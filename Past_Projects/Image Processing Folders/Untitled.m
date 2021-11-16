% This project was designed to have the user click on four corners of one
% of the color folders and have the code determine what color the folder is
% and provide a color mapping of the section

clear all 
close all 
% reading in the image folder01
im = imread('folders01.JPG');

% This takes the RGB image ims and puts each pixel's RGB values in a row.  
% So if you have a million pixels, you'll have a million rows and 3 columns.  
% The first column is the red level, the second is the green level, 
% and the third column is the blue level.
R = im(:,:,1);
G = im(:,:,2);
B = im(:,:,3);

%Show imagine folder01 and name it figure 1
figure(1); imshow(im); axis on;
 
% User have 4 inputs and corrs get stored
% corrdinates are the pixel positions
[x,y] = ginput(4);

%
xM = (x(1)+x(2)+x(3)+x(4)) / 4;
yM = (y(1)+y(2)+y(3)+y(4)) / 4;

%Slope of each line
m_1 = (y(2) - y(1)) / (x(2) - x(1)); % Slope from point 1 to point 2
m_2 = (y(3) - y(2)) / (x(3) - x(2)); % Slope from point 2 to point 3
m_3 = (y(4) - y(3)) / (x(4) - x(3)); % Slope from point 3 to point 4
m_4 = (y(1) - y(4)) / (x(1) - x(4)); % Slope from point 4 to point 1

%Equation of the line between 2 points
b_1 = y(1) - m_1*x(1); % Finding the point of intersection 
b_2 = y(2) - m_2*x(2);
b_3 = y(3) - m_3*x(3);
b_4 = y(4) - m_4*x(4);

%resolution of the picture (height, width)
[x,y] = meshgrid(1:2592,1:1936);

% blacking all of the space that is not inside of the 4 points
%Side one
if (yM < m_1*xM+b_1)
    R(y > m_1*x+b_1) = 0;
    G(y > m_1*x+b_1) = 0;
    B(y > m_1*x+b_1) = 0;
elseif (yM > m_1*xM+b_1)
    R(y < m_1*x+b_1) = 0;
    G(y < m_1*x+b_1) = 0;
    B(y < m_1*x+b_1) = 0;
end

%Side two
if(yM < m_2*xM+b_2)
    R(y > m_2*x+b_2) = 0;
    G(y > m_2*x+b_2) = 0;
    B(y > m_2*x+b_2) = 0;
elseif(yM > m_2*xM+b_2)
    R(y < m_2*x+b_2) = 0;
    G(y < m_2*x+b_2) = 0;
    B(y < m_2*x+b_2) = 0;
end

%side three
if(yM > m_3*xM+b_3)
    R(y < m_3*x+b_3) = 0;
    G(y < m_3*x+b_3) = 0;
    B(y < m_3*x+b_3) = 0;
elseif(yM < m_3*xM+b_3)
    R(y > m_3*x+b_3) = 0;
    G(y > m_3*x+b_3) = 0;
    B(y > m_3*x+b_3) = 0;
end

%side four
if(yM > m_4*xM+b_4)
    R(y < m_4*x+b_4) = 0;
    G(y < m_4*x+b_4) = 0;
    B(y < m_4*x+b_4) = 0;
elseif(yM < m_4*xM+b_4)
    R(y > m_4*x+b_4) = 0;
    G(y > m_4*x+b_4) = 0;
    B(y > m_4*x+b_4) = 0;
end

%reassign the color values to show only the section that was selected
imNew(:,:,1) = R;
imNew(:,:,2) = G;
imNew(:,:,3) = B;
figure(2); imshow(imNew);


figure(3);
image = imNew;
image  = double(reshape(image,[],3));
size(image);
scale = 1:max(image(:));

subplot(3, 1, 1);
hist(image(:,1), scale);
axis([1,255, 0, 200]);
set(get(gca,'children'),'facecolor',[1 0 0])
set(get(gca,'children'),'edgecolor',[1 0 0])

subplot(3, 1, 2);
hist(image(:,2), scale);
axis([1,255, 0, 200]);
set(get(gca,'children'),'facecolor',[0 1 0])
set(get(gca,'children'),'edgecolor',[0 1 0])

subplot(3, 1, 3);
hist(image(:,3), scale);
axis([1,255, 0, 200]);
set(get(gca,'children'),'facecolor',[0 0 1])
set(get(gca,'children'),'edgecolor',[0 0 1])

CR = R(R>0);
CG = G(G>0);
CB = B(B>0);

CR = mean(CR);
CG = mean(CG);
CB = mean(CB);

%Comparing RGB color range to determine what color the folder falls under
if(CR > 251 && CG > 205 && CG < 254 && CB > 89 && CB < 123)
    disp('yellow');
elseif(CR > 93 && CR < 110 && CG > 156 && CG < 174 && CB > 96 && CB < 118)
    disp('green');
elseif(CR > 51 && CR < 82 && CG > 73 && CG < 115 && CB > 89 && CB < 143)
    disp('blue');
elseif(CR > 253 && CG > 116 && CG < 220 && CB > 65 && CB < 93)
    disp('orange');
elseif(CR > 100 && CR < 134 && CG > 75 && CG < 107 && CB > 125 && CB < 166)
    disp('purple');
end
    
%     
% yellow = red > 251 & green>205 & green<254 & blue>89 & blue<123;
% green = red>93 & red<110 & green>156 & green<174 & blue>96 & blue<118;
% blue = red>51 & red<82 & green>73 & green<115 & blue>89 & blue<143;
% orange = red>253 & green>116 & green<220 & blue>65 & blue<93;
% purple = red>100 & red<134 & green>75 & green<107 & blue>125 & blue<166;
% 