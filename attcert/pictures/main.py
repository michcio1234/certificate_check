import abc
import dataclasses
import datetime
from io import BytesIO


@dataclasses.dataclass
class CertificateData:
    name: str
    course: str
    date: datetime.date


class CertificateGenerator(abc.ABC):
    def generate(self, data: CertificateData) -> BytesIO:
        pass


class PDFCertificateGenerator(CertificateGenerator):
    