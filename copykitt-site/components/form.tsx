const Form: React.FC = () => {
  return (
    <>      
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

export default Form; 