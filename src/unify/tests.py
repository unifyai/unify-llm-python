import unittest
from unittest.mock import patch
from clients import Unify, AsyncUnify
import os
from Exceptions import AuthenticationError, KeyError, InternalServerError
from types import GeneratorType, AsyncGeneratorType

class TestUnify(unittest.TestCase):
    def setUp(self):
        # Set up a valid API key for testing
        self.valid_api_key = os.environ.get("UNIFY_KEY")

    def test_invalid_api_key_raises_authentication_error(self):
        # Instantiate Unify with an invalid API key
        with self.assertRaises(AuthenticationError):
            unify = Unify(api_key="invalid_api_key")
            unify.generate("hello")

    @patch('os.environ.get', return_value=None)
    def test_missing_api_key_raises_key_error(self, mock_get):
        # Initializing Unify without providing API key should raise KeyError
        with self.assertRaises(KeyError):
            unify = Unify()
    
    def test_incorrect_model_name_raises_internal_server_error(self):
    # Instantiate Unify with a valid API key
        unify = Unify(self.valid_api_key)
        # Provide incorrect model name to generate function
        with self.assertRaises(InternalServerError):
            unify.generate("hello", "llama-chat")

    def test_generate_returns_string_when_stream_false(self):
        # Instantiate Unify with a valid API key
        unify = Unify(api_key=self.valid_api_key)
        # Call generate with stream=False
        result = unify.generate("hello", stream=False)
        # Assert that the result is a string
        self.assertIsInstance(result, str)

    def test_generate_returns_generator_when_stream_true(self):
        # Instantiate Unify with a valid API key
        unify = Unify(api_key=self.valid_api_key)
        # Call generate with stream=True
        result = unify.generate("hello", stream=True)
        # Assert that the result is a generator
        self.assertIsInstance(result, GeneratorType)
    

class TestAsyncUnify(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        # Set up a valid API key for testing
        self.valid_api_key = os.environ.get("UNIFY_KEY")

    async def test_invalid_api_key_raises_authentication_error(self):
        # Instantiate AsyncUnify with an invalid API key
        with self.assertRaises(AuthenticationError):
            async_unify = AsyncUnify(api_key="invalid_api_key")
            await async_unify.generate("hello")

    @patch('os.environ.get', return_value=None)
    async def test_missing_api_key_raises_key_error(self, mock_get):
        # Initializing AsyncUnify without providing API key should raise KeyError
        with self.assertRaises(KeyError):
            async_unify = AsyncUnify()
            await async_unify.generate("hello")

    async def test_incorrect_model_name_raises_internal_server_error(self):
        # Instantiate AsyncUnify with a valid API key
        async_unify = AsyncUnify(api_key=self.valid_api_key)
        # Provide incorrect model name to generate function
        with self.assertRaises(InternalServerError):
            await async_unify.generate("hello", "llama-chat")

    async def test_generate_returns_string_when_stream_false(self):
        # Instantiate AsyncUnify with a valid API key
        async_unify = AsyncUnify(api_key=self.valid_api_key)
        # Call generate with stream=False
        result = await async_unify.generate("hello", stream=False)
        # Assert that the result is a string
        self.assertIsInstance(result, str)

    async def test_generate_returns_generator_when_stream_true(self):
        # Instantiate AsyncUnify with a valid API key
        async_unify = AsyncUnify(api_key=self.valid_api_key)
        # Call generate with stream=True
        result = await async_unify.generate("hello", stream=True)
        # Assert that the result is a generator
        self.assertIsInstance(result, AsyncGeneratorType)

if __name__ == '__main__':
    unittest.main()