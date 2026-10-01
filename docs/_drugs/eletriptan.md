---
layout: default
title: Eletriptan
parent: 中證據等級 (L3-L4)
nav_order: 307
evidence_level: L4
indication_count: 4
---

# Eletriptan
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Eletriptan：從急性偏頭痛到腦幹先兆偏頭痛

## 一句話總結

Eletriptan 是 5-HT1B/1D 受體促效劑（triptan 類），原本用於急性偏頭痛的治療。
TxGNN 模型預測它可能對**腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 有效，但目前**沒有臨床試驗**，只有 **17 篇偏頭痛相關文獻**，且沒有一篇專門針對腦幹先兆亞型。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性偏頭痛（依文獻；香港許可證資料未載明適應症） |
| 預測新適應症 | 腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的機轉欄位目前缺資料，但文獻顯示 Eletriptan 是 5-HT1B/1D 促效劑，對 5-HT1D 的親和力約為 sumatriptan 的 6 倍，對 5-HT1B 約 3 倍。它原本就用於有先兆和無先兆的偏頭痛，所以模型把它連到偏頭痛的亞型，在生物學上說得通。

不過，這個高分主要反映的是藥物原本就有偏頭痛適應症，並不是發現了新的再利用訊號。現有文獻談的都是一般偏頭痛，沒有針對腦幹先兆。一項 RCT（PMID 15469451）還發現，在先兆期服用 Eletriptan 80 mg 沒有效果。此外，triptan 類藥物因血管收縮的疑慮，傳統上在腦幹先兆偏頭痛中須謹慎使用。

因此，這個預測在機轉上「不矛盾」，但缺乏支持它的直接證據，還有值得警惕的安全性顧慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻多數針對一般偏頭痛，並非腦幹先兆亞型。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | Cephalalgia | 對 sumatriptan 反應不佳或無法耐受的偏頭痛患者（n=446），評估 Eletriptan 的療效與耐受性 |
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT | Eur J Neurol | 在先兆期服用 Eletriptan 80 mg，對後續頭痛沒有效果 |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | Eur Neurol | 比較 Eletriptan 40/80 mg 與 Cafergot 及安慰劑在偏頭痛急性治療的療效、耐受性與安全性 |
| [17501848](https://pubmed.ncbi.nlm.nih.gov/17501848/) | 2007 | RCT 次要分析 | Headache | 評估 Eletriptan 對偏頭痛發作時功能障礙與工作生產力的改善 |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 指引／證據評估 | Headache | 美國頭痛學會對成人急性偏頭痛藥物治療的證據評估 |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Review | Cochrane Database Syst Rev | Eletriptan 用於急性偏頭痛的系統性回顧（另有 2007 年撤回版本） |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatr Drugs | 兒童偏頭痛使用 triptan 類藥物的回顧 |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | 藥物簡介 | Curr Opin Investig Drugs | Eletriptan 為 5-HT1B/1D 促效劑，受體親和力高於 sumatriptan |
| [11050304](https://pubmed.ncbi.nlm.nih.gov/11050304/) | 2000 | 前臨床（體外） | Eur J Pharmacol | 比較 Eletriptan 與 sumatriptan 對人體離體腦膜動脈、冠狀動脈的收縮作用 |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | Case report | Rev Port Cardiol | 一名 53 歲男性服用 Eletriptan 數小時後發生非 ST 段上升型心肌梗塞 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66729 | RELPAX TABLETS 20MG | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據停留在 L4：沒有臨床試驗，文獻談的都是一般偏頭痛，唯一在先兆期給藥的 RCT 結果為無效。
- 高分主要來自藥物本身的既有適應症。而 triptan 在腦幹先兆偏頭痛中傳統上要謹慎使用，有心肌梗塞個案報告，安全性顧慮尚未解決。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選（目前為阻斷性缺口）
- 補齊 DrugBank 的作用機轉資料
- 針對腦幹先兆偏頭痛做專門的文獻回顧，尤其是血管收縮風險
- 確認該亞型是否有可行的臨床試驗設計

**其他預測：** 萎縮性蠕蟲狀皮膚萎縮 (atrophoderma vermiculata)、眉部紅斑角化症 (ulerythema ophryogenes) 及坐骨神經病變 (sciatic neuropathy) 皆為 L5，沒有任何試驗或文獻支持，機轉上也缺乏合理關聯，建議一併 Hold。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

