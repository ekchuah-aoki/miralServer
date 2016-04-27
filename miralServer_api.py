# coding: UTF-8

"""Miral Server API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import endpoints
from protorpc import remote

#アカウント関係
from common.service.AccountService import AccountGetMsg
from common.service.AccountService import AccountGetResMsg
from common.service.AccountService import AccountService

#美容師関係
from beauti.service.BeauticianService import BeautiAccountAddMsg
from beauti.service.BeauticianService import BeautiAccountAddResMsg
from beauti.service.BeauticianService import BeauticianService

#イメージ共通処理関係
from common.service.ImageService  import ImageService
from common.service.ImageService import ImageGetMsg
from common.service.ImageService import ImageGetResMsg 

#美容師免許関連
from beauti.service.LicenseService import LicenseAddMsg
from beauti.service.LicenseService import LicenseAddResMsg
from beauti.service.LicenseService import LicenseService

from common.MiralLogger import MiralLogger


WEB_CLIENT_ID = '1056231959402-bnjsop84r77gdtlrbb68busanr7d2bla.apps.googleusercontent.com'
ANDROID_AUDIENCE = WEB_CLIENT_ID

package='Mirall'


@endpoints.api(name='miralServer', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID,endpoints.API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[endpoints.EMAIL_SCOPE])
class MiralServerApi(remote.Service):
    """MiralServer AIP v1"""

    ########################################
    #アカウント関係
    @endpoints.method(AccountGetMsg, AccountGetResMsg,
                     path='coomon/accountservice/get', http_method='POST',
                     name='common.accountservice.get')

    def common_accountservice_get(self, request): 
        u"""アカウント情報の取得"""
        
        logger = MiralLogger()
        
        logger.debug(u"★"+"param1:"+request.param[0]+ " param2:"+request.param[1])
        
        service = AccountService();
        return service.get(int(request.loginType), request.id)



    ########################################
    #美容師関係
    @endpoints.method(BeautiAccountAddMsg, BeautiAccountAddResMsg,
                     path='beauti/beauticianservice/add', http_method='POST',
                     name='beauti.beauticianservice.add')

    def beauti_beauticianservice_add(self, request): 
        u"""美容師アカウント情報の登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_beauticianservice_add")
        
        service = BeauticianService();
        return service.add(request)
    

    ########################################
    #イメージ共通処理関係
    @endpoints.method(ImageGetMsg, ImageGetResMsg,
                     path='common/imageservice/load', http_method='POST',
                     name='common.imageservice.load')

    def beauti_imageservice_load(self, request): 
        u"""画像データの読み込み"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_imgservice_load")
        logger.debug("fileName:"+str(request.fileName))
        
        service = ImageService();
        return service.load(request.fileName)
    

    """//////////////////////////////////////////////////////
    
    """
    
    @endpoints.method(LicenseAddMsg, LicenseAddResMsg,
                     path='beauti/licenseservice/add', http_method='POST',
                     name='beauti.licenseservice.add')

    def beauti_licenseservice_add(self, request): 
        u"""ライセンス情報の登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_licenseimgservice_save")
        logger.debug("accountId:"+str(request.accountId))
        
        service = LicenseService();
        return service.add(request.accountId, request.imgbase64data)





        
APPLICATION = endpoints.api_server([MiralServerApi])

            
        
    
    
    


