# coding: UTF-8

"""Miral Server API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import endpoints
from protorpc import remote

from common.msg.ApiParamMsg import ApiParamMsg
from common.msg.AccountMsg import AccountMsg
from common.AccountService import AccountService 
from common.MiralLogger import MiralLogger
from beauti.msg.BeautiImageResMsg import BeautiImageResMsg
from beauti.service.LicenseImageService import LicenseImageService
from beauti.msg.BeautiImageMsg import BeautiImageMsg



WEB_CLIENT_ID = '1056231959402-bnjsop84r77gdtlrbb68busanr7d2bla.apps.googleusercontent.com'
ANDROID_AUDIENCE = WEB_CLIENT_ID

package='Mirall'

@endpoints.api(name='miralServer', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID,endpoints.API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[endpoints.EMAIL_SCOPE])
class MiralServerApi(remote.Service):
    """MiralServer AIP v1"""

    """//////////////////////////////////////////////////////
    
    """
    @endpoints.method(ApiParamMsg, AccountMsg,
                     path='coomon/accountservice/get', http_method='POST',
                     name='common.accountservice.get')

    def common_accountservice_get(self, request): 
        u"""アカウント情報の登録"""
        
        logger = MiralLogger()
        
        logger.debug(u"★"+"param1:"+request.param[0]+ " param2:"+request.param[1])
        
        service = AccountService();
        return service.get(int(request.param[0]), request.param[1])

    """//////////////////////////////////////////////////////
    
    """
    @endpoints.method(AccountMsg, AccountMsg,
                     path='coomon/accountservice/add', http_method='POST',
                     name='common.accountservice.add')

    def common_accountservice_add(self, request): 
        u"""アカウント情報の登録"""
        logger = MiralLogger()
        
        logger.debug(u"★common_accountservice_add")
        
        service = AccountService();
        return service.add(request)

    """//////////////////////////////////////////////////////
    
    """
    @endpoints.method(BeautiImageMsg, BeautiImageResMsg,
                     path='beauti/licenseimgservice/add', http_method='POST',
                     name='beauti.licenseimgservice.add')

    def beauti_licenseimgservice_add(self, request): 
        u"""アカウント情報の登録"""
        logger = MiralLogger()
        
        logger.debug(u"★beauti_licenseimgservice_save")
        logger.debug("accountId:"+str(request.accountId))
        
        service = LicenseImageService();
        return service.add(request.accountId, request.imgbase64data)
        
APPLICATION = endpoints.api_server([MiralServerApi])

            
        
    
    
    


