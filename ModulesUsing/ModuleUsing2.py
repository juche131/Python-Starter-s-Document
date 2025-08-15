# Take a look at .\ecommerce\payment\payViaWechat.py
import ecommerce.coupons
# Clearer
from ecommerce.purchase import purchaseObject

# Subpackage
from ecommerce.payment.payViaWechat import pullPayRequest

# Added initializing prints in .\ecommerce\__init__.py and .\ecommerce\payment\payViaWechat.py

# ecommerce initialized, name: ecommerce
# WechatPayment initialized, name: ecommerce.payment.payViaWechat
ecommerce.coupons.BuyXgiveY()
purchaseObject()
pullPayRequest()
print(dir(ecommerce))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'coupons', 'payment', 'purchase']
print(ecommerce.__name__)  # ecommerce
# ModuleSpec(name='ecommerce', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001F55D637770>, origin='d:\\000_PersonalDocuments\\1_StudyMaterials\\Programming\\Python\\Learning\\ModulesUsing\\ecommerce\\__init__.py', submodule_search_locations=['d:\\000_PersonalDocuments\\1_StudyMaterials\\Programming\\Python\\Learning\\ModulesUsing\\ecommerce'])
print(ecommerce.__spec__)
# ['d:\\000_PersonalDocuments\\1_StudyMaterials\\Programming\\Python\\Learning\\ModulesUsing\\ecommerce']
print(ecommerce.__path__)
