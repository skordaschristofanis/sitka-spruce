from argparse import ArgumentParser
from pathlib import Path

from wxmplot.interactive import get_wxapp
from wxutils import AppConfig, WxApplication, add_application_arguments, handle_shortcut_arguments


from .data import get_sitka_files
from .sitka import SitkaFrame


APP_CONFIG = AppConfig(
    name="Sitka",
    assets=str(Path(__file__).resolve().parent / "icons"),
    description="Sitka Hierarchical Data Viewer for HDF5 and Zarr",
    application_id="sitka_spruce.sitka",
)


def sitka_viewer(folder=None):
    """Sitka Viewer for use from a Python/Jupyter REPL."""

    get_wxapp()
    sview = SitkaFrame()
    if folder is not None:
        for fname, dset in get_sitka_files(folder).items():
            sview.add_dataset(fname, dataset=dset)
    sview.Show()
    sview.Raise()
    return sview


def make_parser():
    parser = ArgumentParser(description="Sitka Data Viewer")
    add_application_arguments(parser)
    return parser


def sitka_cli():
    parser = make_parser()
    args = parser.parse_args()

    if handle_shortcut_arguments(parser, args, APP_CONFIG):
        return

    app = WxApplication(APP_CONFIG)
    frame = SitkaFrame(with_inspect=args.inspect)
    app.run(frame)

