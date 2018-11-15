import base64
import io
import tempfile

import matplotlib.pyplot as plt
import wget

from ..core import Widget


class Img(Widget):
    def __init__(self, img):
        super(Img, self).__init__()
        if isinstance(img, plt.Figure):
            self.img = self.fig_to_b64(img)
        elif isinstance(img, str):
            if img.startswith("https://") or img.startswith("http://"):
                img = self.download(img)
            self.img = self.local_to_b64(img)

    def template(self):
        return f'<img src="data:image/png;base64,{self.img}">'

    @staticmethod
    def download(url: str):
        filename = tempfile.mktemp()
        wget.download(url, filename, bar=False)
        return filename

    @staticmethod
    def fig_to_b64(fig: plt.Figure):
        f = io.BytesIO()
        fig.savefig(f, format="png")
        f.seek(0)
        b64 = base64.b64encode(f.read()).decode()
        f.close()
        return b64

    @staticmethod
    def local_to_b64(filename: str):
        with open(filename, "rb") as f:
            return base64.b64encode(f.read()).decode()
