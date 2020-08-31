from django.db import models


class BusinessOwner(models.Model):
    name = models.CharField(max_length=50)
    profile_thumb = models.ImageField(upload_to="profile/")

    def __str__(self) -> str:
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    category = models.CharField(max_length=255)
    address_pin_location = models.TextField()

    def __str__(self) -> str:
        return self.name


class BusinessCampaign(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=4)
    stock_price = models.PositiveIntegerField()
    stock_qty = models.PositiveSmallIntegerField()
    deviden_periode = models.PositiveSmallIntegerField()
    date_ended = models.DateField()

    def __str__(self) -> str:
        return self.title


class CampaignImage(models.Model):
    campaign = models.ForeignKey(BusinessCampaign, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="campaign_images/")

    def __str__(self) -> str:
        # pylint: disable=E1101
        return self.campaign.title