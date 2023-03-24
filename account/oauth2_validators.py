import base64
from oauth2_provider.oauth2_validators import OAuth2Validator
from oauth2_provider.settings import oauth2_settings


class CustomOAuth2Validator(OAuth2Validator):
    oidc_claim_scope = OAuth2Validator.oidc_claim_scope
    oidc_claim_scope.update({
        'email': 'email',
        'profile': 'profile',
    })

    def get_additional_claims(self, request):
        claims = super().get_additional_claims(request)
        if request.user.is_authenticated:
            claims.update({
                'email': request.user.email,
                'last_name': request.user.last_name,
                'first_name': request.user.first_name,
            })
        return claims

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        if request.user.is_authenticated:
            claims.update({
                'email': request.user.email,
                'last_name': request.user.last_name,
                'first_name': request.user.first_name,
            })
        return claims
