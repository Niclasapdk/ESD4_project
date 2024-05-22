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

xlabel('Normalized differential input voltage, $\frac{v_{id}}{V_T}$', 'Interpreter', 'latex','FontSize',14);
ylabel('Normalized collector current, $\frac{i_{C}}{I}$', 'Interpreter','latex','FontSize',14);
set(gca,'FontSize',16);
text(6,0.92,'$\frac{i_{C1}}{I}$','Interpreter','latex','FontSize',20)
text(-6,0.92,'$\frac{i_{C2}}{I}$','Interpreter','latex','FontSize',20)
hold on