clear; close all;
sys1 = tf([1 0 0],[1 2000000/11421 15396]);
sys2 = tf([1.5831E10],[1 177935.9431 1.5831E10]);
bandpass_sys = sys1 * sys2
p = bodeoptions('cstprefs');
p.FreqUnits = 'Hz';
p.YLim = {[-90 5],[-180 180]};
p.Xlim = [1 1E6];
p.PhaseVisible = 'on';
p.TickLabel.FontSize = 14;
p.XLabel.FontSize = 14;
p.YLabel.FontSize = 14;
p.Title.FontSize = 16;
p.Title.String = 'Bandpass Bode Diagram';
bodeplot(bandpass_sys,p);
grid on;