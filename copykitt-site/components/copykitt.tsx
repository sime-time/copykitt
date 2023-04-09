import React from "react"
import Form from "../components/form";
import Results from "../components/results"

const CopyKitt: React.FC = () => {
  const ENDPOINT: string = `https://vsapemn43m.execute-api.us-east-2.amazonaws.com/prod/generate_snippet_and_keywords`
  const [prompt, setPrompt] = React.useState("");
  const [snippet, setSnippet] = React.useState("");
  const [keywords, setKeywords] = React.useState([]);
  const [hasResult, setHasResult] = React.useState(false);

  const onSubmit = () => {
    console.log("Submitting: " + prompt);
    /* execute get command from api */
    fetch(`${ENDPOINT}?prompt=${prompt}`)
      .then((res) => res.json())
      .then(onResult);
  };

  const onResult = (data: any) => {
    setSnippet(data.snippet);
    setKeywords(data.keywords);
    setHasResult(true);
  }

  const onReset = () => {
    setPrompt("");
    setHasResult(false);
  }

  let displayedElement = null; 

  if (hasResult) {
    displayedElement = (<Results prompt={prompt} snippet={snippet} keywords={keywords} onBack={onReset}/>);
  } else {
    displayedElement = (<Form prompt={prompt} setPrompt={setPrompt} onSubmit={onSubmit} />);
  }


  return (
    <>
      <h1>CopyKitt!</h1>
      {displayedElement}
    </>
  );
};

export default CopyKitt;