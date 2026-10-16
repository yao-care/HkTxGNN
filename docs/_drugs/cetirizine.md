---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Cetirizine：預測新適應症為過敏性蕁麻疹 (Allergic Urticaria)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、異位性結膜炎、乳突性結膜炎、春季結膜炎、鼻咽炎、特發性蕁麻疹"
monitor_inn: "Cetirizine"
predicted_indications: ["allergic urticaria", "cold urticaria", "nasal cavity disease", "acute laryngopharyngitis", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
---

# Cetirizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Cetirizine：從過敏性鼻炎等過敏性疾病到過敏性蕁麻疹

## 一句話總結

Cetirizine 是第二代周邊 H1 組織胺受體拮抗劑，原本用於過敏性鼻炎、結膜炎及特發性蕁麻疹等。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，
目前有 **1 個臨床試驗**和 **18 篇文獻**支持這個方向，但該試驗為小型先導研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、異位性結膜炎、乳突性結膜炎、春季結膜炎、鼻咽炎、特發性蕁麻疹（香港許可證未登載適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（依系統評分；實際上僅 1 個樣本數 36 的先導性 Phase 3 試驗，證據強度偏弱，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠資料未收錄）。根據已知資訊，Cetirizine 是選擇性周邊 H1 受體拮抗劑。肥大細胞釋放的組織胺會引起蕁麻疹典型的風團與紅暈反應，H1 阻斷因此直接針對其病理機轉。

原適應症中已包含特發性蕁麻疹，所以過敏性蕁麻疹與已核准用途高度相關。這也與模型的極高預測分數相符。換句話說，這個預測更像是「適應症範圍的延伸」，而非全新的作用方向。

**關於證據等級的提醒：** 唯一的臨床試驗是 36 人的多中心先導可行性研究，評估靜脈注射 cetirizine 對比 diphenhydramine 用於急性蕁麻疹，並非確證療效的大型試驗。因此 L1 的判定應保守解讀。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | 完成 | 36 | 隨機雙盲先導試驗，比較靜脈注射 cetirizine 10 mg 與 diphenhydramine 50 mg 用於急診、緊急照護及過敏門診的急性蕁麻疹，主要驗證可行性 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9506246](https://pubmed.ncbi.nlm.nih.gov/9506246/) | 1998 | Review | Drugs | Fexofenadine 的藥理與臨床回顧（非 cetirizine 專屬） |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Review | Current Medicinal Chemistry | Levocetirizine（cetirizine 的 R-對映異構物）的藥理特性更新 |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine 用於過敏性鼻炎與蕁麻疹 |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine 用於過敏性鼻炎與慢性蕁麻疹 |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clinical Allergy and Immunology | 兒童 H1 抗組織胺：對過敏性鼻結膜炎有一級證據 |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Annals of Pharmacotherapy | 口服抗組織胺用於過敏性鼻炎與慢性特發性蕁麻疹的療效與安全性 |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Cetirizine 對季節性/常年性過敏性鼻炎及慢性特發性蕁麻疹有效且耐受良好 |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine 藥理特性與臨床潛力，標準劑量 10 mg 無中樞抑制作用 |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | 蕁麻疹的成因與治療，非鎮靜抗組織胺為慢性特發性蕁麻疹主要治療 |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | Journal of Clinical Gastroenterology | Cetirizine 引起膽汁鬱積的個案報告（安全性訊號） |

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑。資料中未登載核准適應症與劑型欄位，以下列出其中 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44760 | CETZIE TAB 10MG | 錠劑（依品名） | 未登載 |
| HK-66054 | CETIRIZINE DIHYDROCHLORIDE SANDOZ TABLETS 10MG | 錠劑（依品名） | 未登載 |
| HK-68223 | CETIRIZINE DIHYDROCHLORIDE TABLETS 10MG | 錠劑（依品名） | 未登載 |
| HK-68344 | HOVID CETIRIZINE TABLETS 10MG | 錠劑（依品名） | 未登載 |
| HK-64656 | AXCEL CETIRIZINE SYRUP 5MG/5ML | 糖漿（依品名） | 未登載 |

## 安全性考量

- **知識圖譜標註的潛在禁忌/需謹慎疾病**（非仿單內容）：高血壓、腎臟疾病（含慢性腎病、末期腎衰竭）、肝病、膽囊疾病、糖尿病（含酮酸中毒）、良性前列腺增生、冠狀動脈疾病、動脈粥狀硬化、隅角閉鎖型青光眼、甲狀腺機能亢進（含 Graves 病）。
- **藥物交互作用**：共查得 100 筆，以下為其中中度等級者：bupropion、dronabinol、loperamide、metoclopramide、morphine、nabilone、opium、sibutramine、difenoxin、diphenoxylate。多為中樞神經抑制或相加作用的考量。
- **文獻安全性訊號**：有 1 例 cetirizine 引起膽汁鬱積的個案報告；臨床試驗中曾觀察到 <2% 患者出現暫時性轉胺酶上升。

正式警語與禁忌請以香港衛生署核准仿單為準。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 作用機轉清楚，且蕁麻疹與已核准的特發性蕁麻疹高度相關，預測分數極高。不過目前直接證據只有一個 36 人的先導試驗，且多數文獻為非 cetirizine 專屬的綜述，故需設定防護條件。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症（目前許可證資料缺漏）
- 補足詳細作用機轉資料（MOA）
- 針對過敏性蕁麻疹進行較大規模的確證性 RCT，或取得靜脈注射劑型的後續試驗結果
- 對肝腎功能不全、青光眼、前列腺肥大等族群建立安全性監測計畫

## 其他預測適應症（供參考）

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|-----|-----------|------|---------|------|
| 2 | 寒冷性蕁麻疹 | 99.95% | L3 | Research Question（有小型研究，無登記試驗） |
| 3 | 鼻腔疾病 | 99.77% | L4 | Hold（範圍過廣，需更明確的適應症） |
| 4 | 急性喉咽炎 | 99.72% | L5 | Hold（僅模型預測） |
| 5 | 酒糟性結膜炎 | 99.41% | L5 | Hold（機轉連結薄弱） |
| 6 | 頑固性異位性皮膚炎 | 99.19% | L5 | Hold（抗組織胺效益有限） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

