"""
This file runs the main training/val loop, etc... using Lightning Trainer    
"""

from argparse import ArgumentParser
from pytorch_lightning import Trainer
from pytorch_lightning_dagshub import DAGsHubLogger
import pytorch_lightning_dagshub.utils


def import_model():
    """
    Ugly hack to be able to import the model from ../mnist_model.py
    """
    import os
    examples_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    import sys
    sys.path.append(examples_dir)
    from mnist_model import MnistModel
    return MnistModel


if __name__ == '__main__':
    # Read parameters from a versioned file, which should also be a DVC dependency.
    # This is the purest use case
    hparams_from_file = pytorch_lightning_dagshub.utils.read_hparams('params.yml')

    # OPTIONAL:
    # Allow some hyperparameters to be defined in the command line
    parser = ArgumentParser(add_help=False)
    parser.add_argument('--gpus', type=str, default=None, required=False)

    # Parse args from command line, overriding params from file
    hparams = parser.parse_args(namespace=hparams_from_file)

    MnistModel = import_model()

    # init module
    model = MnistModel(hparams)

    # most basic trainer, uses good defaults
    trainer = Trainer(
        max_nb_epochs=hparams.max_nb_epochs,
        gpus=hparams.gpus,
        val_check_interval=0.2,
        logger=DAGsHubLogger(should_log_hparams=False),  # This is the main point - use the DAGsHub logger!
        default_save_path='lightning_logs',
    )
    trainer.fit(model)
