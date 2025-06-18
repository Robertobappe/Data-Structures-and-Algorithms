import collections
import json
from typing import Any, Optional, List

# Classe para representar um único nó na Árvore Binária de Busca (BST)
class Node:
    def __init__(self, value: Any):       
        #Inicializa um novo nó. Value (Any): O valor a ser armazenado no nó
        self.left: Optional[Node] = None  # Ponteiro para o filho esquerdo
        self.right: Optional[Node] = None # Ponteiro para o filho direito
        self.value: Any = value           # O valor do nó

    def __repr__(self) -> str:
        #Retorna uma representação em string do nó para depuração
        return f"Node(value={self.value})"
    
# Classe para representar a Árvore Binária de Busca (BST)
class BinarySearchTree:
    #Implementa uma Árvore Binária de Busca com operações de inserção,
    #busca, remoção e travessia em largura
    def __init__(self):
        """
        Inicializa uma nova Árvore Binária de Busca com a raiz nula.
        """
        self.root: Optional[Node] = None

    def insert(self, value: Any) -> 'BinarySearchTree':
        """
        Insere um novo valor na BST.
        Mantém a propriedade de BST: valores menores à esquerda, maiores à direita.

        Args:
            value (Any): O valor a ser inserido.

        Returns:
            BinarySearchTree: A instância da BST (para permitir encadeamento de chamadas).
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True: # Loop infinito que será quebrado por um 'return'
                if value < current_node.value:
                    # Ir para a esquerda
                    if current_node.left is None:
                        current_node.left = new_node
                        return self # Inserido, retorna a árvore
                    current_node = current_node.left
                else:
                    # Ir para a direita (inclui valores iguais, que vão para a direita na implementação JS original)
                    if current_node.right is None:
                        current_node.right = new_node
                        return self # Inserido, retorna a árvore
                    current_node = current_node.right

    def lookup(self, value: Any) -> Optional[Node]:
        """
        Procura um valor na BST.

        Args:
            value (Any): O valor a ser procurado.

        Returns:
            Optional[Node]: O nó se o valor for encontrado, ou None caso contrário.
        """
        if self.root is None:
            return None # Árvore vazia, valor não pode ser encontrado

        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else: # current_node.value == value
                return current_node # Valor encontrado
        return None # Valor não encontrado após percorrer a árvore

    def remove(self, value: Any) -> bool:
        """
        Remove um valor da BST.

        Args:
            value (Any): O valor a ser removido.

        Returns:
            bool: True se o valor foi removido com sucesso, False caso contrário.
        """
        if not self.root:
            return False

        current_node = self.root
        parent_node: Optional[Node] = None # Tipo Optional para parent_node
        
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                # Encontramos o nó para remover, vamos trabalhar!

                # Opção 1: Sem filho direito para o nó atual (currentNode)
                if current_node.right is None:
                    if parent_node is None: # O nó a remover é a raiz
                        self.root = current_node.left
                    else:
                        # Se o nó a remover é filho esquerdo do pai
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        # Se o nó a remover é filho direito do pai
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                    return True

                # Opção 2: Filho direito existe, mas não tem filho esquerdo
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left # O filho esquerdo do nó atual se torna o filho esquerdo do nó sucessor
                    if parent_node is None: # O nó a remover é a raiz
                        self.root = current_node.right
                    else:
                        # Se o nó a remover é filho esquerdo do pai
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        # Se o nó a remover é filho direito do pai
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                    return True

                # Opção 3: Filho direito existe e tem um filho esquerdo (o sucessor in-order)
                else:
                    # Encontrar o sucessor in-order (o menor nó na subárvore direita)
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # O filho direito do pai do sucessor se torna o filho direito do sucessor
                    leftmost_parent.left = leftmost.right
                    
                    # Conectar o sucessor in-order à subárvore esquerda e direita do nó a ser removido
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node is None: # O nó a remover é a raiz
                        self.root = leftmost
                    else:
                        # Se o nó a remover é filho esquerdo do pai
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        # Se o nó a remover é filho direito do pai
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
                    return True
        return False # O valor não foi encontrado na árvore


    def breadth_first_search(self) -> List[Any]:
        """
        Realiza uma Busca em Largura (BFS) na árvore e imprime os valores dos nós.

        Returns:
            List[Any]: Uma lista dos valores dos nós na ordem BFS.
        """
        current_node = self.root
        result_list: List[Any] = []
        # Usamos deque para ter operações eficientes de adicionar/remover de ambas as extremidades
        queue: collections.deque[Node] = collections.deque() 

        if current_node: # Adiciona a raiz apenas se ela existir
            queue.append(current_node)

        while queue: # Enquanto a fila não estiver vazia
            current_node = queue.popleft() # Pega o primeiro nó da fila
            print(current_node.value) # Imprime o valor (como no JS)
            result_list.append(current_node.value) # Adiciona ao resultado

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return result_list # Retorna a lista de valores (diferente do JS que apenas imprime)

# --- Função Auxiliar para Visualização da Estrutura da Árvore ---
def traverse_to_dict(node: Optional[Node]) -> Any:
    """
    Função auxiliar recursiva para converter a árvore em uma estrutura de dicionário
    que pode ser facilmente serializada em JSON, similar ao `traverse` do JS.

    Args:
        node (Optional[Node]): O nó atual a ser processado.

    Returns:
        Any: Um dicionário representando o nó e seus filhos, ou None se o nó for None.
    """
    if node is None:
        return None
    
    tree_dict = {"value": node.value}
    tree_dict["left"] = traverse_to_dict(node.left)
    tree_dict["right"] = traverse_to_dict(node.right)
    return tree_dict

# --- Exemplo de Uso (Função main) ---
def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    print("--- Árvore Original ---")
    # Para visualizar a estrutura JSON da árvore, use json.dumps
    print(json.dumps(traverse_to_dict(tree.root), indent=2))
    # Saída esperada (estrutura da árvore):
    #       9
    #      / \
    #     4   20
    #    / \  / \
    #   1   6 15 170

    print("\n--- Buscando valores ---")
    print(f"Buscando 9: {tree.lookup(9)}")
    print(f"Buscando 1: {tree.lookup(1)}")
    print(f"Buscando 170: {tree.lookup(170)}")
    print(f"Buscando 7 (não existe): {tree.lookup(7)}")

    print("\n--- Removendo 170 ---")
    tree.remove(170)
    print(json.dumps(traverse_to_dict(tree.root), indent=2))
    # Saída esperada após remover 170:
    #       9
    #      / \
    #     4   20
    #    / \  /
    #   1   6 15

    print("\n--- Removendo 4 (com 2 filhos) ---")
    tree.remove(4)
    print(json.dumps(traverse_to_dict(tree.root), indent=2))
    # Saída esperada após remover 4 (6 se torna o novo filho à esquerda de 9, 1 se torna filho esquerdo de 6)
    #       9
    #      / \
    #     6   20
    #    /   / \
    #   1   15 None

    print("\n--- Removendo 9 (a raiz) ---")
    tree.remove(9)
    print(json.dumps(traverse_to_dict(tree.root), indent=2))
    # Saída esperada após remover 9 (15 se torna a nova raiz)
    #       15
    #      /  \
    #     6    20
    #    /
    #   1

    print("\n--- Travessia BFS após remoções ---")
    tree.breadth_first_search()
    # Saída esperada (valores impressos):
    # 15
    # 6
    # 20
    # 1

if __name__ == "__main__":
    main()