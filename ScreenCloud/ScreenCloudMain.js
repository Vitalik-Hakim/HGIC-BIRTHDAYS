import { connectScreenCloud } from "@screencloud/apps-sdk";

function start() {
  const refreshTime = 10000;

  setInterval(updateQuote, refreshTime);
  updateQuote();
}

async function start() {
  const sc = await connectScreenCloud();
  const refreshTime = 10000; // This line won't run until the line above finishes successfully.
}
