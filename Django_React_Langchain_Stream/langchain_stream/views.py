from django.shortcuts import render
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging
from .rag_chain import final_chain
# Create your views here.
logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        try:
            logger.info(f"Received message: {message}")
            # Stream the response
            async for chunk in final_chain.astream_events({'question': message}, version="v1", include_names=["Assistant"]):
                logger.info(f"Chunk received: {chunk}")
                if chunk["event"] in ["on_parser_start", "on_parser_stream"]:
                    await self.send(text_data=json.dumps(chunk))

        except Exception as e:
            print(e)
            await self.send(text_data=json.dumps({"error": str(e)}))
