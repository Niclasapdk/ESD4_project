clear; close all;
[FileA,PathA] = uigetfile('*.txt', 'Selec measured frequency reponse with DUT connected');
FullFileA = fullfile(PathA,FileA);
[Freq dB degree] = textread(FullFileA,'%f %f %f','headerlines',1);

figure
yyaxis left
x = Freq;
y = dB;
p = semilogx(x,y);
p.LineWidth = 3;
ylabel('Magnitude [dB]')
yyaxis right
y2 = degree;
p1 = semilogx(x,y2,'--');
p1.LineWidth = 3;
xlabel('Frequency [Hz]');
ylabel('Degree [°]','Interpreter','latex');
title('Bandpass Response');
ax = gca; 
ax.FontSize = 14;
grid on;