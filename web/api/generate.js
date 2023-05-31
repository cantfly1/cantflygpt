module.exports = async (req, res) => {
    const { prompt } = req.body;
  
    // Validez le prompt
    if (!prompt) {
      return res.status(400).send({ error: 'No prompt provided' });
    }
  
    // Appelez votre serveur backend avec le prompt
    // Pour le moment, nous renvoyons simplement le prompt
    const task = `Generated task for prompt: ${prompt}`;
  
    res.status(200).send({ task });
  };