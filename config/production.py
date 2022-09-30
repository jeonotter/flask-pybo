from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'*\x02\xb7\xbb\xc3\x8e\xc9\x08\xafB1\x99\x0b1\x97\xd2'
