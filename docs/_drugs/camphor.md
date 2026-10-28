---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Camphor：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：目前缺乏已登錄的核准適應症文字"
monitor_inn: "Camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
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

## Camphor（樟腦）：從外用止痛與抗刺激製劑到偏頭痛
{: .text-alpha }

## 一句話總結

Camphor 是多種外用軟膏、藥膏、膏藥與藥油的成分，在香港有 20 張有效許可證。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效。
目前**沒有臨床試驗**，僅有 **3 篇間接文獻**（皆為病例報告、病例系列或回顧），另有一篇 2026 年動物實驗支持相近的偏頭痛亞型。證據仍屬研究假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前缺乏已登錄的核准適應症文字（許可證資料中適應症欄位皆為空白） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Camphor 是 TRPV1、TRPA1、TRPM8 的調節劑，外用時具有抗刺激（counter-irritant）、清涼與止痛作用。這些受器與疼痛傳導相關，因此機轉上可能與頭痛的疼痛路徑有關。

在偏頭痛的相關研究中，直接證據很少：
- 2026 年一項動物實驗（PMID 42849823）指出，天然 (+)-camphor 可緩解利血平誘發、伴隨局部腦血管痙攣的偏頭痛模型，可能透過抑制 p38β MAPK/ATF2 路徑。這項證據屬於「偏頭痛感受性（migraine with or without aura, susceptibility to）」這個預測項目，是目前最直接的機轉線索。
- Camphor 也是菊蒿（feverfew）精油的成分，而菊蒿是傳統的偏頭痛草藥，但這只是間接關聯。
- 另有病例報告顯示，含樟腦與尤加利精油的牙膏與叢集性頭痛發作在時間上相關，這反而提示 Camphor 可能**誘發**或加重頭痛，而不是治療頭痛。

整體而言，0.9985 的分數只是計算預測，並非臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | 病例報告 | BMJ Case Reports | 2 例叢集性頭痛與使用含樟腦、尤加利精油的牙膏在時間上相關 |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | 病例系列 | Headache | 5 例叢集性頭痛與含促痙攣精油的牙膏相關；精油可能誘發癲癇並使偏頭痛惡化 |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | 回顧 | Z Kinder Jugendpsychiatr Psychother | 1940–50 年代兒童與青少年神經精神藥物治療的歷史分析，與樟腦偏頭痛療效無直接關係 |

**補充（相關預測項目）：** 針對「偏頭痛感受性」的動物研究（PMID 42849823，2026 年，*Journal of Ethnopharmacology*），顯示天然 (+)-camphor 在利血平誘發的偏頭痛模型中有緩解作用。這是前臨床證據，非人體研究。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58885 | MENTHOLATUM OINT | 未登載 | 未登載 |
| HK-58884 | MENTHOLATUM OINT | 未登載 | 未登載 |
| HK-54063 | KUMMEL OINTMENT | 未登載 | 未登載 |
| HK-31313 | DELTAPHOR LOTION | 未登載 | 未登載 |
| HK-55838 | VICKS VAPORUB OINT | 未登載 | 未登載 |

以上列出 5 張主要許可證，共 20 張有效單一成分許可證，無已註銷者。從品名可知多為外用的軟膏、乳膏、藥油、噴霧或貼布。

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，本次彙整的預測資料指出：
- 有病例報告顯示含樟腦精油與叢集性頭痛發作相關，可能加重頭痛。
- 樟腦在較高劑量下具神經毒性（有癲癇風險）。
- 一項大鼠口服急性毒性研究（PMID 27955803）觀察到組織氧化壓力與病理變化，提示口服的安全顧慮。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛的證據僅有前臨床動物實驗與間接病例報告，沒有任何人體臨床試驗；而且部分病例報告提示樟腦可能誘發頭痛，與預測方向相反。
- 作用機轉資料與安全性資料都有缺口，目前只適合列為研究問題。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉（MOA）與香港衛生署仿單的警語、禁忌資料
- 確認各許可證的核准適應症與劑型
- 評估外用與頭痛部位使用的可行性（吸收、皮膚刺激、神經毒性風險）
- 進一步的動物實驗驗證，再設計小規模探索性臨床試驗
- 釐清樟腦究竟是緩解還是誘發頭痛的劑量與暴露條件
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

