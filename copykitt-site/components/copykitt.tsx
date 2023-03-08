import React from "react"

const CopyKitt: React.FC = () => {
  const [prompt, setPrompt] = React.useState("");

  const onSubmit = () => {
    console.log("Submitting: " + prompt);
    /* execute get command from api */
    fetch
  };
  
  return (
    <>
      <h1>CopyKitt!</h1>
      <p>Tell me what your brand is about and I will generate copy and keywords for you.</p>
      <input 
        type="text" 
        placeholder="coffee" 
        value={prompt}
        onChange={(e) => setPrompt(e.currentTarget.value)}
      ></input>
      <button onClick={onSubmit}>Submit</button>
    </>
  );
};

export default CopyKitt;