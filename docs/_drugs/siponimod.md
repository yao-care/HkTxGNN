---
layout: default
title: Siponimod
parent: 僅模型預測 (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Siponimod：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：資料未載明"
---

# Siponimod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Siponimod：從（原適應症未載明）到肺動脈高壓

## 一句話總結

Siponimod 是一種 S1P 受體調節劑，在香港以 MAYZENT 錠劑上市，但本次整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，預測分數很高，但目前**沒有臨床試驗和文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Siponimod 是選擇性 S1P1/S1P5 受體調節劑，S1P 訊號與肺血管重塑及內皮屏障功能有關，因此在機轉上有理論上的關聯。

不過，Siponimod 與肺動脈高壓之間沒有已記載的直接連結。S1P 受體調節劑也可能引起心搏過緩，並影響心血管與肺部功能，因此這個預測的安全性令人擔憂。

整體而言，這個預測目前只是模型輸出，缺乏臨床或文獻佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測適應症概況

以下為 TxGNN 其他高分預測，供後續優先排序參考：

| 排名 | 預測適應症 | 分數 | 證據等級 | 備註 |
|------|-----------|------|---------|------|
| 2 | 偏頭痛 (Migraine disorder) | 99.66% | L4 | 僅有 1 篇間接個案報告，另 1 篇為泛論性神經科回顧 |
| 4 | 腦幹型先兆偏頭痛 | 99.56% | L4 | 僅有間接文獻 |
| 5 | 偏頭痛易感性 | 99.49% | L4 | 為遺傳易感性分類詞，非可治療的臨床實體 |
| 7 | 類風濕性關節炎 | 99.16% | L4 | 有 S1P 訊號在免疫疾病的回顧，機轉合理但無 RA 專屬資料；建議列為研究問題 |
| 10 | 骨髓增生異常症候群 | 98.79% | L5 | 淋巴球下降效應可能加重血球低下與感染風險 |

其餘預測（脊柱後凸性心臟病、Prinzmetal 心絞痛、萎縮性蠕蟲狀皮膚病、眉部紅斑性毛囊角化症）皆僅有模型預測，無機轉依據或臨床證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66876 | MAYZENT TABLETS 2MG | 未載明 | 未載明 |

持證商為 NOVARTIS PHARMACEUTICALS (HK) LIMITED。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下列出部分主要項目：
  - **重大 (Major)**：Famotidine、Ranitidine、Cimetidine、Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、Aprepitant、Clarithromycin、Dolasetron、Palonosetron、Oxandrolone、Levofloxacin
  - **中度 (Moderate)**：Loperamide、Bisacodyl、Picosulfuric acid、Sodium sulfate、Naltrexone、Polyethylene glycol (3350 含電解質)
- **機轉相關的安全疑慮**：S1P 受體調節劑可能引起心搏過緩與房室傳導影響，對心血管類適應症（如肺動脈高壓、Prinzmetal 心絞痛）需特別審慎。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 肺動脈高壓的預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- Siponimod 的心臟相關風險使心肺類適應症的風險效益不明確。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料（MOA）
- 進行 S1P 訊號與肺血管重塑的前臨床研究，並評估心血管安全性
- 若要尋找較有潛力的方向，可優先評估類風濕性關節炎等免疫相關適應症，並系統性檢索偏頭痛相關的直接證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

