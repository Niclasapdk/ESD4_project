close all; clear;
[FileA1,PathA1] = uigetfile('*.txt', 'Selec measured frequency reponse with DUT connected');
FullFileA1 = fullfile(PathA1,FileA1);
[Freq1 dBfund1 dBfund2 dBfund3] = textread(FullFileA1,'%f %f %f %f','headerlines',1);

subplot(2,1,1);
s = semilogx(Freq1, dBfund1, Freq1, dBfund2);
xlabel('Frequency [Hz]','FontSize',12);
ylabel('Magnitude [dB]','FontSize',12);
axis([0 25000, 0 70]);
s(1).LineWidth = 1.4;
s(2).LineWidth = 1.4;
legend({'Line Level Gain Stage','RIAA'},'FontSize',14);
set(gca,'FontSize',14);
set(gca ,'xticklabel',[])
xlabel('');
grid on;
title('Complete System')
hold on;
subplot(2,1,2);
s1 = semilogx(Freq1, dBfund3);
s1(1).Color = 'm';
xlabel('Frequency [Hz]','FontSize',12);
ylabel('Magnitude [dB]','FontSize',12);
axis([0 25000, 0 70]);
s1(1).LineWidth = 1.4;
legend({'RIAA'},'FontSize',14);
set(gca,'FontSize',14);
title('Only RIAA');
grid on;