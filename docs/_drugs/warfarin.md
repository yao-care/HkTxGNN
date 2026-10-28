---
layout: default
title: Warfarin
parent: 僅模型預測 (L5)
nav_order: 944
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "Warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Warfarin：預測新適應症為肝素輔因子 II 缺乏症 (heparin cofactor 2 deficiency)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Warfarin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Warfarin: 肝素輔因子 II 缺乏症 (heparin cofactor 2 deficiency)
{: .text-alpha }

## 一句話總結

Warfarin（華法林）是口服維生素 K 拮抗型抗凝血劑，原本用於肺栓塞、血栓性疾病與顱內栓塞。
TxGNN 模型預測它可能對**肝素輔因子 II 缺乏症 (Heparin Cofactor 2 Deficiency)** 有效，但目前僅有 **3 篇個案報告**，**沒有臨床試驗**支持。這類預測大多屬於既有血栓適應症的延伸，而非全新機轉。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肝素輔因子 II 缺乏症 (heparin cofactor 2 deficiency) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依藥理學常識，Warfarin 抑制維生素 K 依賴的凝血因子（II、VII、IX、X）合成，從而降低血栓形成風險。

肝素輔因子 II 缺乏症是一種遺傳性血栓傾向，患者容易反覆發生靜脈或心臟內血栓。Warfarin 的作用位於凝血抑制物的下游，因此在這類患者作為血栓後的長期預防用藥，機轉上說得通。

不過這與 Warfarin 已核准的血栓性疾病適應症屬同一機轉，較像是**既有適應症類別內的延伸**，而非真正的新機轉再利用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | 個案報告 | Kyobu Geka | 14 歲女性家族性肝素輔因子 II 缺乏，右心室出現血栓 |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | 個案報告 | Nihon Kyobu Shikkan Gakkai Zasshi | 先天性抗凝血酶缺乏併肺梗塞，曾使用 Warfarin 治療 7 年 |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | 個案報告（家族） | Journal of UOEH | 家族多發血栓，患童開始 Warfarin 後仍再發深層靜脈血栓 |

這些報告僅描述病例，無法證明 Warfarin 對此疾病的療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41422 | WARFARIN TAB 3MG (TEVA) | — | 資料未載明 |
| HK-61443 | ORFARIN TABLETS 3MG | — | 資料未載明 |
| HK-41423 | WARFARIN TAB 5MG (TEVA) | — | 資料未載明 |
| HK-41421 | WARFARIN TAB 1MG (TEVA) | — | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單文字）：高血壓、肝衰竭／肝病、膽囊疾病、充血性心衰竭、甲狀腺功能低下、腎病症候群、腎功能不全、精神疾病、結締組織疾病、骨病、物質濫用／依賴、凝血疾病、高血脂、貧血、膽汁鬱積、慢性腹瀉等。
- **藥物交互作用**：共查得 100 筆，以下為部分示例。
  - **嚴重（Major）**：乙醯水楊酸（Aspirin）、Metronidazole
  - **中度（Moderate）**：Ranitidine、Rabeprazole、Doxycycline、Hydrocortisone、Dexamethasone、Metformin、Amoxicillin、Bupropion、Aprepitant 等

詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅限於 3 篇個案報告，無臨床試驗，且個案中甚至有 Warfarin 治療下仍再發血栓的情形。
- 此預測屬既有血栓適應症的延伸，新增價值有限。

**若要推進需要：**
- 取得 Warfarin 的作用機轉資料與香港仿單（警語、禁忌、核准適應症）
- 針對肝素輔因子 II 缺乏症的族群，進行回溯性世代研究或系統性回顧，評估 Warfarin 的療效與出血風險
- 與現行指引及直接口服抗凝血劑（DOAC）比較，釐清其臨床定位

---

### 附註：其他預測適應症（供參考）

| 排名 | 預測適應症 | 分數 | 證據等級 | 決策 | 說明 |
|------|-----------|------|---------|------|------|
| 2 | 第五因子過多伴自發性血栓 | 0.9984 | L5 | Hold | 無試驗或文獻，僅有模型預測 |
| 3 | 抗凝血酶缺乏症第 2 型 | 0.9984 | L5 | Hold | 僅有 1 篇個案報告，未顯示療效 |
| 4 | 血栓傾向 (Thrombophilia) | 0.9975 | L2 | Research Question | 有 1 個 Phase 3 試驗（NCT00895505，D-dimer 引導延長預防，狀態不明、無結果），間接相關，主要為既有適應症延伸 |
| 5 | 類風濕性關節炎 | 0.9921 | L4 | Hold | 4 個 Phase 1 試驗皆為藥物交互作用研究，無療效證據 |
| 6 | 乳房纖維囊腫 | 0.9920 | L5 | Hold | 僅有 Danazol 交互作用個案，分數可能反映交互作用訊號 |
| 7 | 良性乳腺發育不良 | 0.9910 | L5 | Hold | 上一項的同義詞，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據 |

其中**類風濕性關節炎**及**乳房疾病**的高分很可能來自藥物交互作用的共現訊號，而非療效，不建議作為再利用方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

