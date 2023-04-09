import React from "react"
import Form from "../components/form";
import Results from "../components/results"

const CopyKitt: React.FC = () => {
  const ENDPOINT: string = `https://vsapemn43m.execute-api.us-east-2.amazonaws.com/prod/generate_snippet_and_keywords`
  const CHAR_LIMIT: number = 32;
  const [prompt, setPrompt] = React.useState("");
  const [snippet, setSnippet] = React.useState("");
  const [keywords, setKeywords] = React.useState([]);
  const [hasResult, setHasResult] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(false);

  const onSubmit = () => {
    console.log("Submitting: " + prompt);
    setIsLoading(true);
    /* execute get command from api */
    fetch(`${ENDPOINT}?prompt=${prompt}`)
      .then((res) => res.json())
      .then(onResult);
  };

  const onResult = (data: any) => {
    setSnippet(data.snippet);
    setKeywords(data.keywords);
    setHasResult(true);
    setIsLoading(false);
  }

  const onReset = () => {
    setPrompt("");
    setHasResult(false);
    setIsLoading(false);
  }

  let displayedElement = null; 

  if (hasResult) {
    displayedElement = (<Results prompt={prompt} snippet={snippet} keywords={keywords} onBack={onReset}/>);
  } else {
    displayedElement = (<Form prompt={prompt} setPrompt={setPrompt} onSubmit={onSubmit} isLoading={isLoading} characterLimit={CHAR_LIMIT}/>);
  }


  return (
    <>
      <h1>CopyKitt!</h1>
      {displayedElement}
    </>
  );
};

export default CopyKitt;