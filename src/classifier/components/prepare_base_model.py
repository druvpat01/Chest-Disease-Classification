from classifier.config.configuration import ConfigManager
from classifier.entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf
from pathlib import Path

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        """
            prepares VGG16 as the base model
        """

        # NOTE: we are taking a model without the Fully Connected Layers.
        # Model only has Convolution Layers
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,      # [224, 224, 3]
            weights=self.config.params_weights,             # 'imagenet' - weights trained on imagenet dataset
            include_top=self.config.params_include_top      # removes the fully-connecter(Dense) layers if False
        )

        self.save_model(path=self.config.base_model_path, model=self.model)
    
    @staticmethod
    def prepare_final_model(model, classes, freeze_all, freeze_till, learning_rate):

        # fixing the models weights
        if freeze_all:      # no weights are trained
            for layer in model.layers:
                model.trainable = False

        elif (freeze_till is  not None) and (freeze_till > 0):  # some weights are trained
            for layer in model.layers[: -freeze_till]:
                model.trainable = False

        # output shape: flatten the outlayer: (None, 7,7,512) -> (None, 25088) 'None' is the batch size
        outputs = tf.keras.layers.Flatten()(model.output)
        
        # Creating a Dense layer for binary Classification i.e 2 classes  
        predcition = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(outputs)

        # adding the Dense layer with our model
        final_model = tf.keras.models.Model(
            inputs=model.input,     # input shape: (None, 224, 224, 3) in our case
            outputs=predcition      # output shape: (None, 2) -> for binary classification
        )

        # providing an optimizer, loss function and  metrics to evaluate for training
        final_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate), # using SGD to optimize the weights
            loss=tf.keras.losses.CategoricalCrossentropy(),                 # cross entropy loss function
            metrics=['accuracy']
        )       

        final_model.summary()   # prints the summary of the final model.
        return final_model
    
    def update_base_model(self):
        """     Moddifies and saves the base model      """
        self.final_model = self.prepare_final_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(self.config.updated_base_model_path, self.final_model)

    def save_model(self, path: Path, model: tf.keras.Model):
        """     Saves the model to the provided path    """
        model.save(path)