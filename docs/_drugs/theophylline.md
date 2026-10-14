---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 871
evidence_level: L5
indication_count: 5
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Theophylline：從氣喘到血栓性疾病

## 一句話總結

Theophylline（茶鹼）是一種黃嘌呤類支氣管擴張劑，原本用於氣喘、支氣管炎、肺氣腫等呼吸道疾病。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic Disease)** 有效，但目前**沒有任何臨床試驗**，檢索到的 **19 篇文獻**也幾乎都與此用途無關，證據僅停留在模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、支氣管炎、肺氣腫等呼吸道疾病（香港許可證未載明適應症文字，此處依知識圖譜的適應症資料） |
| 預測新適應症 | 血栓性疾病 (Thrombotic Disease) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張（皆為有效的單一成分製劑） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Theophylline 是非選擇性磷酸二酯酶 (PDE) 抑制劑，同時也是腺苷受體拮抗劑。目前缺乏藥物資料庫中的詳細作用機轉資料，以上是根據其已知藥理特性所作的說明。

在血小板中，PDE 受抑制會使 cAMP 上升，理論上可以抑制血小板聚集。這是它與血栓形成之間的潛在機轉連結。不過這條連結只是推論，原適應症（呼吸道疾病）與血栓性疾病在病理上差異很大。

TxGNN 給出 0.996 的高分，但這純屬計算預測。檢索到的文獻大多與主題不符，例如抗血小板藥 ticlopidine 的藥物動力學、血小板標記物檢測、血液 microRNA 樣本處理，以及茶鹼的檢測感測器。沒有任何一篇評估 theophylline 預防或治療血栓。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表為檢索到的文獻中相對較相關者，沒有 RCT，以回顧性文章為先。**這些文獻沒有一篇直接證明 theophylline 對血栓性疾病有效。**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | 抗血小板藥 ticlopidine 的藥物動力學，與 theophylline 無直接關係 |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | 前列腺素、血小板與動脈粥狀硬化；說明 cAMP 上升可抑制血小板聚集 |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | 離體研究 | Rheumatology (Oxford) | Behçet 氏症患者的血小板與嗜中性球活化，與年齡、性別及疾病活動度的關係 |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 藥理研究 | General Pharmacology | Milrinone 與腺苷合併抑制人類血小板反應，機轉上與 cAMP 路徑相關 |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | 檢測研究 | Platelets | 血漿可溶性 CLEC-2 的測定，作為血小板活化標記 |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | 方法學研究 | PLoS One | 最佳化血漿製備以監測血小板儲存分子 |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | 方法學研究 | Cells | 抗凝劑與樣本處理對血液 microRNA 定量的影響 |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | 觀察性研究 | Inflammatory Bowel Diseases | 發炎性腸道疾病患者的血小板-白血球聚集 |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | 檢測研究 | British Journal of Haematology | 血小板第 4 因子放射免疫分析；theophylline 僅作為檢體製備中的添加劑 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 分析方法開發 | Analytica Chimica Acta | 茶鹼電化學適體感測器，與治療血栓無關 |

---

## 香港上市資訊

香港共有 8 張有效許可證，皆為單一成分製劑，以下列出 5 張。資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45955 | SLO-THEO CAP 100MG (EXTENDED-RELEASE) | 緩釋膠囊（依品名） | — |
| HK-19359 | NUELIN-SR 125 TAB 125MG S R WHITE | 緩釋錠（依品名） | — |
| HK-45832 | NUELIN SR 300 TAB 300MG (INDIA) | 緩釋錠（依品名） | — |
| HK-45831 | NUELIN SR 200 TAB 200MG (INDIA) | 緩釋錠（依品名） | — |
| HK-45954 | SLO-THEO CAP 50MG (EXTENDED-RELEASE) | 緩釋膠囊（依品名） | — |

---

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單內容）**：知識圖譜中與 theophylline 相關的禁忌或需謹慎的疾病包括高血壓、肝衰竭與肝病、癲癇、焦慮與精神疾病（含思覺失調類）、紫質症、腎臟病、消化性潰瘍、開角型青光眼、甲狀腺功能低下、糖尿病（含酮酸中毒）、良性前列腺肥大、血小板減少、嗜中性球減少及顆粒球缺乏等。此清單僅供參考，實際禁忌請以原廠仿單為準。
- **藥物交互作用**：共記錄 100 筆。
  - **重大 (Major)**：Bupropion。
  - **中度 (Moderate)**：Clarithromycin、Cimetidine、Famotidine、Ranitidine、Omeprazole、Rabeprazole、Doxycycline、Tetracycline、Minocycline、Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、活性碳等。
  - **輕微 (Minor)**：Ephedrine。
- **治療窗狹窄**：theophylline 血中濃度過高易中毒，臨床上需監測血中濃度。個體間代謝差異（如 CYP1A2 基因多型）也會影響劑量。

其餘警語請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只來自模型計算，沒有臨床試驗，檢索到的文獻也沒有直接評估 theophylline 對血栓的作用，證據等級僅 L5。
- 機轉上雖有 cAMP 抑制血小板的理論連結，但很薄弱。theophylline 治療窗狹窄、交互作用多，而現有的抗血栓藥物已經很成熟，貿然推進並不合理。

**若要推進需要：**
- 先做前臨床或離體研究，確認 theophylline 在可達到的安全血中濃度下能否抑制血小板聚集或血栓形成。
- 取得詳細的作用機轉資料，並補齊香港原廠仿單的警語與禁忌資料。
- 若前臨床結果正向，再設計小型探索性臨床試驗，並規劃血中濃度監測與抗血小板、抗凝血藥物的交互作用評估。

**補充：** 同一批預測中，「阻塞性肺病 (Obstructive Lung Disease)」有多個已完成的 Phase 3 試驗，但那屬於 theophylline 的原有適應症，並非真正的新用途。「鼻腔疾病」和「氣管疾病」證據較少，可列為後續研究方向，血栓性疾病則不是目前的優先選項。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

