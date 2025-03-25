from redisvl.extensions.router import Route
import os
from redisvl.extensions.router import SemanticRouter
from redisvl.utils.vectorize import HFTextVectorizer
import logging
from config import ROUTER_NAME, REDIS_URL, REDIS_SOCKET_CONNECT_TIMEOUT, REDIS_SOCKET_TIMEOUT

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

genai_programming = Route(
    name="genai_programming",
    description="GenAI Programming Topics",
    references=[
        "Best practices for fine-tuning language models",
        "Fine-tuning language models best practices",
        "Language model fine-tuning techniques and practices",
        "Fine-tuning best practices for large language models",
        "Best practices in language model fine-tuning",
        "Building conversational AI with transformer models",
        "Developing conversational agents using transformers",
        "Transformer-based conversational AI implementation",
        "Creating conversational AI systems with transformers",
        "Conversational AI development with transformer models",
        "Vector database optimization for semantic search",
        "Optimizing vector databases for semantic search",
        "Semantic search optimization in vector databases",
        "Vector database performance optimization",
        "Optimizing semantic search with vector databases",
        "How to implement RAG with Python and vector databases",
        "Python implementation of RAG with vector databases",
        "Building RAG systems using Python and vector databases",
        "Vector database implementation for RAG in Python",
        "RAG system development with Python and vector databases",
        "Python code for RAG with vector database integration",
        "Implementing RAG using Python and vector databases",
        "Vector database setup for RAG in Python",
        "RAG implementation guide with Python and vector databases",
        "Python RAG system with vector database backend",
        "Implementing RAG (Retrieval Augmented Generation) with Python",
        "Building RAG systems with vector databases",
        "Vector database integration for RAG applications",
        "Python implementation of RAG with vector search",
        "Using vector databases for semantic search in RAG",
        "RAG architecture with vector embeddings",
        "Vector similarity search in RAG systems",
        "Python libraries for RAG implementation",
        "Vector database setup for RAG applications",
        "RAG system optimization with vector databases",
        "Prompt engineering techniques for GPT-4",
        "Methods for evaluating LLM outputs",
        "Token optimization strategies for large language models",
        "Techniques for preventing hallucinations in generative AI",
        "Python programming for AI and machine learning",
        "Software development with AI tools",
        "Programming best practices for AI applications",
        "Debugging and testing AI systems",
        "AI model deployment and scaling",
        "Programming languages for AI development"
    ],
    metadata={"category": "programming", "priority": 1},
    distance_threshold=0.1
)

scifi_entertainment = Route(
    name="scifi_entertainment",
    description="Science Fiction Entertainment",
    references=[
        "Time travel concepts in modern science fiction",
        "Modern sci-fi exploration of time travel",
        "Time travel themes in contemporary science fiction",
        "Contemporary sci-fi and time travel concepts",
        "Time travel in modern science fiction media",
        "Modern science fiction time travel narratives",
        "AI consciousness and themes in Westworld",
        "Westworld's exploration of artificial intelligence",
        "Consciousness and AI in science fiction",
        "Artificial intelligence themes in Westworld",
        "AI and consciousness in modern sci-fi",
        "Westworld's approach to AI consciousness",
        "Blade Runner's influence on cyberpunk genre and themes",
        "Star Trek: The Original Series and its impact on sci-fi",
        "Star Trek: The Next Generation and its themes",
        "Star Trek: Deep Space Nine and its character development",
        "Star Trek: Voyager and its exploration themes",
        "Star Trek: Enterprise and its prequel storyline",
        "Star Trek: Discovery and its modern take on the franchise",
        "Star Trek: Picard and its continuation of TNG",
        "Star Trek: Strange New Worlds and its episodic format",
        "Star Trek: Lower Decks and its animated comedy",
        "Star Trek: Prodigy and its family-friendly approach",
        "Cyberpunk genre development and themes",
        "Time travel in science fiction movies and TV",
        "Dystopian futures in Blade Runner and its sequel",
        "Time travel paradoxes in sci-fi movies",
        "Alien contact narratives in modern television",
        "Cyberpunk themes in Netflix's Altered Carbon",
        "Space exploration in The Expanse series",
        "Post-apocalyptic survival in Mad Max: Fury Road",
        "Science fiction books and novels",
        "Sci-fi TV shows and series",
        "Science fiction movies and films",
        "Futuristic technology in entertainment",
        "Space and time travel stories",
        "Science fiction themes and tropes",
        "Cyberpunk genre evolution and influence",
        "Time travel storytelling in science fiction",
        "Modern sci-fi series and their themes"
    ],
    metadata={"category": "entertainment", "priority": 1},
    distance_threshold=0.1
)

classical_music = Route(
    name="classical_music",
    description="Classical Music",
    references=[
        "How to analyze Mozart's opera compositions",
        "Analyzing Mozart's opera works and compositions",
        "Mozart's opera composition techniques and analysis",
        "Opera composition analysis in Mozart's works",
        "Analyzing Mozart's operatic compositions",
        "Understanding Bach's baroque music techniques",
        "Bach's baroque music techniques and analysis",
        "Baroque music techniques in Bach's compositions",
        "Analyzing Bach's baroque musical techniques",
        "Bach's approach to baroque music composition",
        "Storytelling through classical music lyrics and composition",
        "Narrative techniques in classical music and opera",
        "Lyrics and storytelling in classical vocal music",
        "Classical music as a storytelling medium",
        "Opera librettos and musical storytelling",
        "Vocal music and narrative in classical compositions",
        "Storytelling elements in classical music lyrics",
        "Classical music lyrics and their narrative structure",
        "Musical storytelling in classical vocal works",
        "Lyrics and narrative in classical choral music",
        "Beethoven's evolution from Classical to Romantic periods",
        "Mozart's approach to opera composition",
        "Comparing Bach's and Handel's baroque techniques",
        "The influence of Russian folk music on Tchaikovsky",
        "Debussy's innovations in impressionist music",
        "Evolution of the symphony from Haydn to Mahler",
        "Chamber music in the late Romantic period",
        "Stravinsky's revolutionary approach to rhythm and harmony",
        "Classical music composers and their works",
        "Orchestral music and symphonies",
        "Classical music history and periods",
        "Opera and vocal music",
        "Classical music instruments and ensembles",
        "Music theory and composition"
    ],
    metadata={"category": "music", "priority": 1},
    distance_threshold=0.15
)

# Initialize the SemanticRouter
router = SemanticRouter(
    name=ROUTER_NAME,
    vectorizer=HFTextVectorizer(),
    routes=[scifi_entertainment, genai_programming, classical_music],
    redis_url=REDIS_URL,
    overwrite=True,
    socket_connect_timeout=REDIS_SOCKET_CONNECT_TIMEOUT,
    socket_timeout=REDIS_SOCKET_TIMEOUT
)

def test_route(query):
    logger.info(f"\nTesting query: {query}")
    response = router.route_many(query)
    if response:
        logger.info(f"Matched route: {response[0].name}, Similarity score: {response[0].distance}")
    else:
        logger.info("No matching route found")
        
# Test with various queries
# Classical Music queries
test_route("Storytelling techniques in classical music lyrics")  # Should match classical_music
test_route("Beethoven's influence on Romantic period music")  # Should match classical_music
test_route("How to analyze Mozart's opera compositions")  # Should match classical_music
test_route("Understanding Bach's baroque music techniques")  # Should match classical_music
test_route("The evolution of symphonic music from Haydn to Mahler")  # Should match classical_music

# GenAI Programming queries
test_route("How to implement RAG with Python and vector databases")  # Should match genai_programming
test_route("Best practices for fine-tuning language models")  # Should match genai_programming
test_route("Prompt engineering techniques for GPT-4")  # Should match genai_programming
test_route("Building a conversational AI with transformers")  # Should match genai_programming
test_route("Vector database optimization for semantic search")  # Should match genai_programming

# SciFi Entertainment queries
test_route("The latest Star Trek series and its themes")  # Should match scifi_entertainment
test_route("Blade Runner's influence on cyberpunk genre")  # Should match scifi_entertainment
test_route("Time travel concepts in modern sci-fi")  # Should match scifi_entertainment
test_route("The Expanse's approach to space exploration")  # Should match scifi_entertainment
test_route("AI and consciousness themes in Westworld")  # Should match scifi_entertainment

# Unrelated queries (should not match)
test_route("how do I change my oil in my car")
test_route("Need help with Outlook configuration")
test_route("Best Italian restaurants in New York")
test_route("How to train for a marathon")
test_route("Tips for growing tomatoes in your garden")
