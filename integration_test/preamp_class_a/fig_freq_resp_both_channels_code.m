clear; close all;
[File1,Path1] = uigetfile('*.csv', 'left channel');
FullFile1 = fullfile(Path1,File1);
Tb1 = readtable(FullFile1);
[File2,Path2] = uigetfile('*.csv', 'right channel');
FullFile2 = fullfile(Path2,File2);
Tb2 = readtable(FullFile2);
subplot(2,1,1);
s = semilogx(Tb1,"Frequency_Hz_","Channel2Magnitude_dB_");
title('Class A Frequency Reponse Right Channel');
grid on;
s(1).LineWidth = 3;
s(1).Color = 'k';
xlabel('');
ylabel('Channel 2 Magnitude [dB]')
set(gca,'FontSize',14);
set(gca ,'xticklabel',[])
hold on;
subplot(2,1,2);
s1 = semilogx(Tb2,"Frequency_Hz_","Channel2Magnitude_dB_");
grid on;
s1(1).LineWidth = 3;
s1(1).Color = 'b';
set(gca,'FontSize',14);
title('Left Channel');
xlabel('Frequency [Hz]');
ylabel('Channel 2 Magnitude [dB]')
%%SØDE KAT !!