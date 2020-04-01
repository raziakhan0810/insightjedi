import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from insightjedi_app.models import Document
from insightjedi_app.serializers.document import DocumentSerializer

logger = logging.getLogger(__name__)


def get_document_data(document_data):
    data = DocumentSerializer(document_data).data
    return data


class DocumentAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datas = []
        try:
            all_data = Document.objects.all()
            if all_data is not None:
                for document in all_data:
                    result = get_document_data(document)
                    datas.append(result)
                return Response({'data': datas})
            else:
                return Response({'message': 'No records found!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while getting document data: {}'.format(ex))

    def post(self, request):
        owner = request.data.get('owner')
        type = request.data.get('type')
        source_type = request.data.get('source_type')
        source_id = request.data.get('source_id')
        input_meta_data = request.data.get('input_meta_data')
        try:
            document = Document.objects.create(
                owner=owner,
                type=type,
                source_type=source_type,
                source_id=source_id,
                input_meta_data=input_meta_data
            )
            document.save()
            return Response({'success': 'Document created successfully!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while creating document data: {}'.format(ex))

    def delete(self, request):
        document_id = request.data.get('document_id')
        try:
            document = Document.objects.get(id=document_id)
            document.delete()
            return Response({'message': 'Document deleted successfully!!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.exception('Error while deleting document data: {}'.format(ex))
