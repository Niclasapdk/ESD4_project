%% Sigmoid for Nouglas :)
clear all; clc;
a = 1;
b = 1;
c = -0.001;

x = linspace(-10,10,400);
sigmoid = a./(1+exp(-b*(x-c)));

figure(5), clf
plot(x, sigmoid, 'linew',3);
hold on
plot([0 0],get(gca, 'ylim'),'k--','LineWidth',1)
hold on
plot(-x, sigmoid, 'linew',3);
hold on
plot([0.8 0.8],get(gca, 'ylim'),'k--','LineWidth',1)
hold on
plot([-0.8 -0.8],get(gca, 'ylim'),'k--','LineWidth',1)
hold on
plot([-10 0],[0.5 0.5],'--k','LineWidth',1);
xlabel('Normalized differential input voltage','FontSize',14);
ylabel('Normalized collector current','FontSize',14);
set(gca,'FontSize',16);
hold on