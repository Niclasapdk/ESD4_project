close all; clear;
[FileA1,PathA1] = uigetfile('*.txt', 'Selec measured frequency reponse with DUT connected');
FullFileA1 = fullfile(PathA1,FileA1);
[Freq1 dBfund1 dBfund2 dBfund3] = textread(FullFileA1,'%f %f %f %f','headerlines',1);

s = semilogx(Freq1, dBfund1, Freq1, dBfund2);
xlabel('Frequency(Hz)','FontSize',12);
ylabel('dB scale','FontSize',12);
axis([0 25000, 0 70]);
s(1).LineWidth = 1.4;
s(2).LineWidth = 1.4;
legend({'Line Level Gain Stage','RIAA stage'},'FontSize',16);
set(gca,'FontSize',16);
grid on;