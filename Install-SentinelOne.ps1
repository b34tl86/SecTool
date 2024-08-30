#Enter the SentinelOne site token here, within the quotes.
$SentinelSiteToken = "eyJ1cmwiOiAiaHR0cHM6Ly9ldWNlMS1uaW5qYW9uZS5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiYjRlNjc5ODQ4NWEwNzI3ZiJ9";

#fill in a publicly available download URl for your SentinelOne *EXE* 64-bit installer here. An Azure blob with a SAS link works well!
$SentinelDownloadUrl = "";
#this folder will be used or created, feel free to change it. This variable should not have a trailing \
$tempPath = "\\192.168.1.250\FolderDeployment\Installer\SentinelOne\";
#the script will save the SentinelOne installer as "S1.exe" in the above named folder
$SentinelPath = "$tempPath\SentinelOneInstaller_windows_64bit_v23_4_4_223.exe";

function TempPath
{
    if(Test-Path $tempPath)
    {
        Remove-Item "$tempPath\*";
    }
    else
    {
        New-Item $tempPath -ItemType Directory;
    }
}

function SentinelInstall
{
    If ((Get-WmiObject win32_operatingsystem | Select-Object osarchitecture).osarchitecture -eq "64-bit")
    {
        Set-Location $tempPath;
        (New-Object Net.WebClient).DownloadFile($SentinelDownloadUrl, $SentinelPath);
        Start-Process S1.exe -ArgumentList "/SILENT /SITE_TOKEN=$SentinelSiteToken"
    }
    else {
        Exit 1;
    }
}

TempPath;
SentinelInstall;