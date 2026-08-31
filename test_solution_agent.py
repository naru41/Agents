import unittest

from solution_agent import run


class SolutionAgentTest(unittest.IsolatedAsyncioTestCase):
    async def test_dispatches_request_and_preserves_any_output(self):
        received = []

        async def dispatch(system_prompt, request):
            received.append((system_prompt, request))
            return '{"kind":"patch","files":["extension/popup.js"]}'

        output = await run({"prompt": "  ขอเฉลย  ", "context": {"mode": "scratch"}}, dispatch)

        self.assertIn("auxiliary solution agent", received[0][0])
        self.assertEqual(received[0][1], {"prompt": "ขอเฉลย", "context": {"mode": "scratch"}})
        self.assertEqual(output, {"kind": "patch", "files": ["extension/popup.js"]})


if __name__ == "__main__":
    unittest.main()
