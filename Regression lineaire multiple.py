import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

#On génère un dataset

x, y = make_regression(n_samples=100, n_features = 2, noise=10)

plt.scatter(x[:, 0], y)

#Si vous utiliser jupyter lab (ce que je vous conseil, ici vous aurez un tableau en 2 dimensions qui vous affichera votre dataset grace au plt.scatter juste au-dessus
#Vous pourrez donc voir à quoi ressemble votre dataset

# Verificaation des dimensions
print(x.shape)
print(y.shape)

#Redéfinition de la matrice y
y = y.reshape(y.shape[0], 1)
print(y.shape)

#Ici les fonctions print vous afficheront les dimmensions des matrices x, y utilisées

#matrice X
X = np.hstack((x, np.ones((x.shape[0], 1))))
print(X.shape)
print(X[:10])

#Au dessus, on initialise la matrice x en X et on y integre une colonne de biais égale à 1 pour nos futurs calculs, pour que l'or de la résolution de l'équation f(ax +b) a est associés à x et la colonne de biais 1 à b

theta = np.random.randn(3, 1)
theta

#On initialise la variable THETA cette varaible nous servira à ajuster d'autres paramètres par la suite, vous obtenez un tableau de [3,1]

#Calcul du modèle:

def model(X, theta):
    return X.dot(theta)
model(X, theta)

#Grace à la variable theta on ajuste le modele à la matrice X pour la suite des calculs
  
plt.scatter(x[:, 0], y)
plt.scatter(x[:, 0], model(X, theta))

#Un petit coup de plt.scatter pour jetter un oeil à notre dataset avec la courbe d'apprentissage....bon ce n'est pas encore cela mais nous sommes sur la bonne voie
#Encore une fois utilisez jupyter si vous etes debutant en python, sinon vous pouvez utiliser spyder ou vs code mais si vous ne savez pas vous servir de python je vous conseille d'executer les fonctions une par une pour bien comprendre
#Sur notre courbe actuelle on voit bien que l'apprentissage n'est pas encore au point que faut-il faire ?

#Fonction coût

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

#Ceci est la fonction coût, pour faire simple voyez l'équation quadratique moyenne

#Calcul du gradient

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)
    
#Le calcul de gradient nous aidera pour la descente de gradients

#Calcul de la descente de gradient

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history
    
#Voici la descente de gradients qui va nous permettre d'ajuster notre calcul et nous tracer une belle courbe d'apprentissage

#Machine learning !
n_iterations = 1000
learning_rate = 0.1

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate=0.01, n_iterations=1000)

#maintenant on rassemble tout dans des variables (theta_final sera la variable theta avec le meilleur "ajustement") on effectue la descente de gradient, le learning_rate et le nb d'itération nous permet d'avoir une meilleur precision sur le calcul cela depend de notre dataset

predictions = model(X, theta_final)
plt.scatter(x[:, 0], y)
plt.scatter(x[:, 0], predictions, c='r')

#On verifie la prediction avec matplotlib
#Ici vous aurez un jolie tableau avec votre dataset et par dessus chaque point du dataset VOTRE courbe d'apprentissage qui correspond a peut pres au dataset meme plutot tres bien si vous suivez le dataset de cette exemple.

from mpl_toolkits.mplot3d import Axes3D
%matplotlib notebook
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[:, 0], x[:, 1], y)
ax.scatter(x[:, 0], x[:, 1], predictions)

#Je vous mets de quoi avoir un graphique en 3d car nous sommes en regression multiples donc le tableau en 2D que vous avez vu juste avant n'est pas complet il vous manque la 3eme dimension sur le coté droit du tableau 2D
# Avec cela vous aurez une meilleur vu d'ensemble de votre modèle d'apprentissage

plt.plot(range(1000), cost_history)

#Grace au cost_hostory vous pouvez maintenant voir l'évolutiion de votre courbe d'apprentissage, c'est aussi ici que vous pouvez ajuster votre learning_rate et nb_iterations

# Coef de détermination

def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v
    
#Et bien sur votre coef de determination, de cette manière vous saurez si bvotre modele d'apprentissage est fiable ou non ;) bonne chance les amis !!


