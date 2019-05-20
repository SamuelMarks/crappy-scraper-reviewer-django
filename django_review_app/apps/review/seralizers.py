from rest_framework import serializers

from django_review_app.apps.review.models import Review


class ReviewSerializer(serializers.Serializer):
    created = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    urls = serializers.CharField()
    named_entities = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Review` instance, given the validated data.
        """
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Review` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.title)
        instance.title = validated_data.get('title', instance.code)
        instance.urls = validated_data.get('urls', instance.linenos)
        instance.named_entities = validated_data.get('named_entities', instance.language)
        instance.save()
        return instance
