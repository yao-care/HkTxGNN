---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
monitor_inn: "ROTIGOTINE"
predicted_indications: ["attention deficit-hyperactivity disorder", "schizophrenia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "faciodigitogenital syndrome", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "atypical glycine encephalopathy", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited"]
last_modified_at: 2026-10-23
description: "Rotigotine：預測新適應症為注意力不足過動症 (ADHD)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯：不寧腿症候群、帕金森氏症及多種帕金森類症候群"
---

# Rotigotine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Rotigotine：從帕金森氏症到注意力不足過動症
{: .text-alpha }

## 一句話總結

Rotigotine 是一種多巴胺受體促效劑，知識圖譜中記錄的用途包括不寧腿症候群與帕金森氏症。
TxGNN 模型預測它可能對**注意力不足過動症 (ADHD)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇間接相關文獻**，且皆未直接研究 rotigotine 治療 ADHD，屬於早期研究假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯：不寧腿症候群、帕金森氏症及多種帕金森類症候群（香港許可證未載明適應症文字） |
| 預測新適應症 | 注意力不足過動症 (ADHD) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，rotigotine 是多巴胺受體促效劑（涵蓋 D1–D5，對 D3 親和力較高），也作用於部分血清素與腎上腺素受體。

ADHD 與多巴胺及去甲腎上腺素系統失調有關。其中一篇文獻探討多巴胺 D4 受體與 α2A 腎上腺素受體的異聚化，與 ADHD 的遺傳關聯相關，提供了合理但間接的生物學連結。另外兩篇文獻是不寧腿症候群的回顧，僅因不寧腿症與 ADHD 常共病、且共享多巴胺藥理而相關。

需要強調：沒有任何已引用的研究直接評估 rotigotine 對 ADHD 的療效，因此證據等級只能判定為 L5（僅有模型預測）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | 不寧腿症候群的回顧，描述其臨床特徵與盛行率（約 2–3%） |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | 兒童不寧腿症候群的藥物治療選項回顧 |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | 前臨床／機轉研究 | Pharmacological research | α2A 腎上腺素受體與多巴胺 D4 受體變異體的異聚化，與衝動控制疾患及 ADHD 相關 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55447 | NEUPRO TRANSDERMAL PATCH 2MG/24H | 未載明 | 未載明 |
| HK-55444 | NEUPRO TRANSDERMAL PATCH 8MG/24H | 未載明 | 未載明 |
| HK-55446 | NEUPRO TRANSDERMAL PATCH 4MG/24H | 未載明 | 未載明 |
| HK-55445 | NEUPRO TRANSDERMAL PATCH 6MG/24H | 未載明 | 未載明 |

以上 4 張皆為單一成分製劑，持有者為 UCB PHARMA (HONG KONG) LIMITED，目前均為有效狀態。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單文字）：高血壓、多系統萎縮症、姿勢性直立心搏過速症候群、姿勢性低血壓、藥物誘發的異動症。
- **藥物交互作用**：共查得 51 筆，以下為部分中度等級者：
  - 嗎啡、可待因、鴉片、地芬諾辛、diphenoxylate（中樞神經抑制疊加）
  - 乙醇（酒精）
  - 抗組織胺類：promethazine、chlorpheniramine、cetirizine、brompheniramine、carbinoxamine、clemastine、azelastine（鼻用）
  - 甲氧氯普胺 (metoclopramide)（與多巴胺促效劑藥理拮抗）
  - dronabinol、nabilone、sibutramine、dextromethorphan
  - ioflupane I-123（可能干擾顯影判讀）

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也未直接研究 rotigotine 對 ADHD 的療效，只有間接的受體機轉與不寧腿症共病線索，證據等級為 L5。
- 知識圖譜記錄了高血壓、姿勢性低血壓等禁忌關聯，且 ADHD 族群以兒童與青少年居多，安全性疑慮需先釐清。

**若要推進需要：**
- 取得 rotigotine 的作用機轉資料，並評估其在 ADHD 相關神經迴路的合理性。
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選。
- 進行 rotigotine 於 ADHD 的前臨床或探索性臨床研究（例如先在不寧腿症合併 ADHD 的族群中觀察）。
- 評估貼片劑型是否適合目標族群（尤其是兒童），以及心血管與直立性低血壓風險的監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

