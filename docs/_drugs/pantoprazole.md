---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pantoprazole：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L5）。原適應症：消化性潰瘍、胃食道逆流、食道炎、Zollinger-Ellison 症候群等"
---

# Pantoprazole
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

# Pantoprazole：從消化性潰瘍／胃食道逆流到活動性消化性潰瘍

## 一句話總結

Pantoprazole 是質子幫浦抑制劑（PPI），原本用於消化性潰瘍、胃食道逆流、食道炎及 Zollinger-Ellison 症候群等胃酸相關疾病。
TxGNN 模型預測它對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，目前有 **1 個已完成的 Phase 3 臨床試驗**和 **多篇文獻**支持。
需要說明的是，此預測屬於既有適應症的範圍，實際上不是真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化性潰瘍、胃食道逆流、食道炎、Zollinger-Ellison 症候群等（取自知識圖譜） |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L1（依資料編譯結果；僅 1 個已完成的 Phase 3 試驗，嚴格依本報告判定規則應為 L2，詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

> 證據等級說明：依判定規則，L1 需要 ≥2 個已完成的 Phase 3 RCT。目前僅有 1 個已完成的 Phase 3 試驗（NCT02084420），且 Pantoprazole 在該試驗中可能是對照組。文獻中另有數項相關的隨機對照試驗，但多屬間接證據。因此保守來看，證據強度介於 L1 與 L2 之間。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠資料欄位未收錄）。不過依據已知藥理，Pantoprazole 會不可逆地抑制胃壁細胞上的 H+/K+ ATPase（質子幫浦），這是胃酸分泌的最後一步，因此能降低胃酸、讓潰瘍癒合。

活動性消化性潰瘍本來就是 Pantoprazole 的核心適應症，所以模型給出高分（99.69%）並不意外。這個預測反映的是模型正確辨認出藥物既有的用途，而非發現新用途。

其他排名較低的預測（潰瘍穿孔、胃空腸潰瘍、十二指腸胃逆流、十二指腸阻塞）的證據強度逐步遞減，詳見結論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 完成 | 323 | 多中心、隨機、雙盲、活性對照試驗，比較 Ilaprazole 與 Pantoprazole 三合療法（7 天）對胃／十二指腸潰瘍合併幽門螺旋桿菌感染患者的根除效果；Pantoprazole 為試驗藥或對照藥需進一步確認 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 LA 分級 C/D 食道炎的療效與安全性 |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut Liver | Tegoprazan 治療內視鏡切除後人工潰瘍（非 Pantoprazole 專屬） |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | 比較研究 | Am J Gastroenterol | 巴西多中心研究，比較 Pantoprazole 與 Ranitidine 治療十二指腸潰瘍 |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | 比較研究 | Hepato-gastroenterology | 比較 Lansoprazole 與 Pantoprazole 治療活動性十二指腸潰瘍及根除幽門螺旋桿菌 |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole 作用持續時間長，且尚未發現明確藥物交互作用 |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Review | Med Arh | PPI 用於胃食道逆流的治療 |
| [10450061](https://pubmed.ncbi.nlm.nih.gov/10450061/) | 1999 | Review | Pharmacology | 各 PPI 在同毫克劑量下劑量反應與效力相近 |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Review | Int J Clin Pharmacol Ther | CYP2C19 多型性對 PPI 作用的影響 |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | 動物實驗 | Inflammopharmacology | Pantoprazole 併用間質幹細胞對大鼠胃潰瘍的癒合作用 |
| [26439477](https://pubmed.ncbi.nlm.nih.gov/26439477/) | 2016 | 動物實驗 | J Nat Med | 藏紅花素對大鼠吲哚美辛誘發胃損傷的保護作用（Pantoprazole 為對照） |

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單方製劑，目前無已註銷者。以下列出 5 張主要許可證（資料中未收錄劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44676 | PANTOLOC I.V. INJ 40MG（Takeda） | 注射劑 | 未提供 |
| HK-45019 | PANTOLOC GASTRO-RESISTANT TAB 20MG（Takeda） | 腸溶錠 | 未提供 |
| HK-63999 | TECTA GASTRO-RESISTANT TABLETS 40MG（Takeda） | 腸溶錠 | 未提供 |
| HK-59424 | PANTOPRAZOLE SANDOZ TAB 20MG（Sandoz） | 錠劑 | 未提供 |
| HK-64263 | PANRAZOL ENTERIC COATED TABLETS 20MG（Teva） | 腸溶錠 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：骨質疏鬆、停經後骨質疏鬆、骨折、惡性貧血（此為圖譜關聯，並非仿單文字，臨床上多與長期使用 PPI 的骨質及維生素 B12 吸收風險有關）
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Acalabrutinib、Atazanavir
  - **中度 (Moderate)**：Alpelisib、Amphotericin B、Atorvastatin、Bosutinib、Fenofibrate、Hydrochlorothiazide、Bumetanide 等
  - **輕微 (Minor)**：Acetylsalicylic acid、Cyanocobalamin、Axitinib、Bortezomib 等

其他警語與仿單禁忌症，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 活動性消化性潰瘍屬 Pantoprazole 的既有核心適應症，機轉明確，且有 Phase 3 試驗與多篇臨床文獻支持，同時香港已有 20 張有效許可證。
- 此項屬於「既有適應症確認」而非真正的新適應症，且仿單層級的安全性資料尚未取得。

**其他預測適應症概況：**

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 潰瘍穿孔 | 99.63% | L3 | 研究性問題；Pantoprazole 僅為手術修補後的輔助用藥 |
| 胃空腸潰瘍 | 99.63% | L4 | 研究性問題；文獻皆為間接證據（壓力性潰瘍預防等） |
| 十二指腸胃逆流 | 99.27% | L3 | 研究性問題；僅有小型生理／觀察性研究，對膽汁逆流本身的作用不明 |
| 十二指腸阻塞 | 99.21% | L5 | Hold；無明確機轉關聯，僅有一篇非評估 Pantoprazole 的病例報告 |

**若要推進需要：**
- 取得香港衛生署的仿單資料（警語、禁忌症、核准適應症），這是目前阻擋安全性篩查的缺口
- 補齊作用機轉（MOA）的正式資料
- 確認 NCT02084420 中 Pantoprazole 是試驗藥還是對照藥
- 針對長期使用的骨質疏鬆、骨折與維生素 B12 缺乏風險，建立監測計畫
- 評估與 Atazanavir、Acalabrutinib 等重大交互作用藥物併用時的處理原則
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

