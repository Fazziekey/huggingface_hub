from app.pipelines.base import Pipeline, PipelineException  # isort:skip

from app.pipelines.audio_source_separation import AudioSourceSeparationPipeline
from app.pipelines.automatic_speech_recognition import (
    AutomaticSpeechRecognitionPipeline,
)
from app.pipelines.feature_extraction import FeatureExtractionPipeline
from app.pipelines.image_classification import ImageClassificationPipeline
from app.pipelines.question_answering import QuestionAnsweringPipeline
from app.pipelines.sentence_similarity import SentenceSimilarityPipeline
from app.pipelines.text_classification import TextClassificationPipeline
from app.pipelines.text_to_speech import TextToSpeechPipeline
from app.pipelines.token_classification import TokenClassificationPipeline
