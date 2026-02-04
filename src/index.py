from endee import Endee,Precision
from embed import get_embedding_dimension as ged

def create_index(name="docs"):
	client = Endee()
	if not client.exists(name):
		client.create_index(
			name = name,
			dimension = ged(),
			space_type = "cosine",
			precision = Precision.INT8D

		)
	return client.get_index(name)


