from .models import UpdatedFiles, Semestar, Fakultet, Smjer
from rest_framework import serializers


class UpdatedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedFiles
        fields = ['title', 'link', 'date', 'subjecttag', 'webtag']


class SemestarSerializer(serializers.ModelSerializer):
    # smjer = serializers.SlugRelatedField(
    #     queryset=Smjer.objects.all(),
    #     read_only=False,
    #     slug_field='smjer'
    # )

    # fakultet = serializers.SlugRelatedField(
    #     queryset=Fakultet.objects.all(),
    #     read_only=False,
    #     slug_field='fakultet'
    # )
    smjer = serializers.CharField()
    fakultet = serializers.CharField()

    class Meta:
        model = Semestar
        fields = ['fakultet', 'smjer', 'semestar', 'resultlink']

    def create(self, validated_data):
        smjer = validated_data.pop('smjer')
        fakultet = validated_data.pop('fakultet')

        smjer_instance, created = Smjer.objects.get_or_create(smjer=smjer)
        fakultet_instance, created = Fakultet.objects.get_or_create(fakultet=fakultet)

        semestar_instance = Semestar.objects.create(**validated_data, fakultet=fakultet_instance, smjer=smjer_instance)
        return semestar_instance
