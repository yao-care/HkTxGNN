---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 9
monitor_inn: "CARBOPLATIN"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-10-27
description: "Carboplatin：預測新適應症為直腸黏液腺癌 (rectum mucinous adenocarcinoma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Carboplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Carboplatin：鉑類細胞毒性化療藥物 → 直腸黏液腺癌 (rectum mucinous adenocarcinoma)
{: .text-alpha }

## 一句話總結

Carboplatin（卡鉑）是鉑類細胞毒性化療藥物，目前在香港有多張有效許可證。
TxGNN 模型預測它可能對**直腸黏液腺癌 (rectum mucinous adenocarcinoma)** 有效，預測分數為 0.9928。
但本報告整理的資料中**沒有任何直接相關的臨床試驗或文獻**，這個預測目前僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 直腸黏液腺癌 (rectum mucinous adenocarcinoma) |
| TxGNN 預測分數 | 0.9928 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Carboplatin 屬於鉑類化療藥物，一般認為其作用方式是造成 DNA 損傷、抑制腫瘤細胞分裂。這只是藥物類別層面的通則，並非針對直腸黏液腺癌的機轉證據。

這項預測的依據，主要是模型從黏液性腺癌的共同組織型態推得的高分，並非來自直接的臨床或機轉研究。本次查詢沒有找到針對直腸黏液腺癌使用 carboplatin 的試驗或文獻。

因此，這個預測的合理性仍待驗證。黏液性腺癌常被認為對化療反應較差，這一點也需要在後續評估中特別留意。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港市場狀態：已上市。所有登記的許可證均為單一成分製劑且仍有效。以下列出部分主要許可證：

| 許可證號 | 品名 | 製造商／持有商 |
|---------|------|-----------|
| HK-35025 | PARAPLATIN INJ 10MG/ML | DKSH Hong Kong Limited |
| HK-61610 | CARBOPLATIN CONCENTRATE FOR SOLUTION FOR INFUSION 450MG/45ML | Hong Kong Medical Supplies Ltd |
| HK-60146 | KEMOCARB INJ 450MG/45ML | Fresenius Kabi Hong Kong Limited |
| HK-66515 | CARBOPLATIN-TRANET CONCENTRATE FOR SOLUTION FOR INFUSION 450MG/45ML | The International Medical Company Limited |
| HK-65993 | CARBOPLATIN MYLAN CONCENTRATE FOR SOLUTION FOR INFUSION 150MG/15ML | Viatris Healthcare Hong Kong Limited |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（鉑類） |
| 骨髓抑制風險 | 高（為鉑類藥物的主要劑量限制性毒性，常見血小板與嗜中性白血球減少） |
| 致吐性分級 | 中至高（依劑量而異） |
| 監測項目 | CBC（含分類與血小板）、腎功能、肝功能、電解質；留意神經病變與聽力變化 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

上述內容依藥物類別的一般認知整理，非取自本次彙整的原廠仿單資料。實際使用請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：本次彙整的資料顯示共有 100 筆交互作用紀錄，以下為已列出的主要項目。
  - 中度：質子幫浦抑制劑（rabeprazole、omeprazole、esomeprazole、lansoprazole、dexlansoprazole、pantoprazole）、胺基糖苷類抗生素（kanamycin、neomycin、streptomycin）、vancomycin、metronidazole、tinidazole、rosuvastatin、simvastatin。
  - 輕度：levofloxacin。
- **需謹慎評估的疾病狀態**（未經仿單確認）：腎臟疾病、肝臟疾病、血小板減少、嗜中性白血球減少、貧血、白血球減少、周邊神經病變、凝血異常、聽力障礙。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測目前只有模型分數支持，沒有任何針對直腸黏液腺癌的臨床試驗或文獻，證據等級為 L5。
- 黏液性腺癌的化療反應可能較差，且缺乏作用機轉資料，現階段不宜推進。

**若要推進需要：**
- 搜尋並確認 carboplatin 用於直腸（或大腸）黏液腺癌的臨床或觀察性研究。
- 補充詳細的作用機轉資料，並評估黏液性組織型態對鉑類藥物的敏感性。
- 取得香港原廠仿單的警語與禁忌症資料，完成安全性評估。
- 與標準治療比較，評估臨床上是否有納入 carboplatin 的需求。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

