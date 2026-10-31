---
layout: default
title: Ephedrine
parent: 中證據等級 (L3-L4)
nav_order: 326
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Ephedrine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia"]
description: "Ephedrine：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L4）。原適應症：本地許可證資料未記載適應症"
---

# Ephedrine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

## Ephedrine: 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Ephedrine（麻黃素）是擬交感神經藥物，原本用於過敏性鼻炎、血管運動性鼻炎、咽炎、感冒等上呼吸道相關症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇**較舊或品質有限的文獻，且此預測與既有適應症高度重疊，並非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Ephedrine 是間接作用為主、同時具直接 α/β 腎上腺素受體促效作用的擬交感神經藥物，可使鼻黏膜血管收縮、減輕充血與水腫。

鼻腔疾病與其原有的鼻炎、鼻咽炎等適應症在部位與病理上密切相關，因此機轉上合理。但也要注意，這個預測大部分與既有適應症重疊，並不是真正新穎的再利用方向，高分（0.999）很可能反映的正是與已知適應症的近似性。

另一個較低排名的預測是三叉神經自律神經性頭痛（分數 0.9934，機轉連結薄弱，且擬交感神經藥物可能誘發或加重頭痛、升高血壓，風險效益不利）。此預測僅有模型分數支持，證據等級為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | 臨床試驗（與抗組織胺複方） | Svenska lakartidningen | 於鼻腔試驗 N-hydroxyethylpromethazine 與 ephedrine 的複方，無摘要可供判讀 |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | 初步臨床觀察 | Zhongguo Zhong xi yi jie he za zhi | 探討鼻炎噴劑治療慢性鼻炎的臨床效果；是否含 ephedrine 無法僅從標題確認，且可能無對照 |

這兩篇文獻證據力皆偏弱：一篇為 1960 年代的複方試驗，另一篇為可能無對照的初步觀察。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-14664 | EPHEDRINE SULPHATE INJ 30MG/ML | 注射劑（依品名） | 資料未提供 |
| HK-20794 | EPHEDRINE NASAL DROPS 1% | 滴鼻劑（依品名） | 資料未提供 |
| HK-39223 | EFMOL NASAL DROPS 1% | 滴鼻劑（依品名） | 資料未提供 |
| HK-65424 | EPHEDRINE HYDROCHLORIDE SOLUTION FOR INJECTION 30MG/1ML | 注射劑（依品名） | 資料未提供 |
| HK-23992 | MECODIN COUGH SYRUP | 糖漿（依品名） | 資料未提供 |

香港共有 20 張有效的單方許可證，包含注射劑、滴鼻劑、錠劑及咳嗽糖漿等多種產品，無已註銷者。以上僅列出其中 5 張。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來源為知識圖譜關聯，非仿單文字）：高血壓、充血性心衰竭、肝衰竭、肝病、腎病、癲癇、慢性阻塞性肺病、消化性潰瘍、胃潰瘍、焦慮症、精神疾病（含思覺失調類）、紫質症、甲狀腺功能低下、開角型青光眼、發炎性腸道疾病、胰臟炎、膽囊疾病、血小板低下等。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分主要者：
  - 重大 (Major)：Tramadol、Amitriptyline、Bupropion、Methylene blue
  - 中度 (Moderate)：Formoterol、Salbutamol、Arformoterol、Methylphenidate、Amphetamine、Atomoxetine、Atenolol、Acebutolol、Metformin 等
  - 輕微 (Minor)：Morphine、Ascorbic acid

仿單層級的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的鼻腔疾病與既有適應症（鼻炎、鼻咽炎）高度重疊，不構成真正的新適應症；現有證據僅有兩篇薄弱文獻，無臨床試驗，證據等級 L4。
- 其他預測（三叉神經自律神經性頭痛）僅有模型分數支持，且風險效益不利。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認各產品的核准適應症、警語與禁忌
- 補充 DrugBank 的作用機轉資料
- 釐清此預測相對於現有適應症的實質新增價值，並進行系統性文獻回顧
- 針對高血壓、心血管疾病等族群擬定安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

