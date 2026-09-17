---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 806
evidence_level: L5
indication_count: 5
---

# Zidovudine
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

# Zidovudine：從 HIV 感染到猴免疫缺陷病毒感染

## 一句話總結

> Zidovudine（AZT，DB00495）是史上第一個核苷類反轉錄酶抑制劑（NRTI），原始核准用於人類免疫缺陷病毒（HIV）感染／後天免疫缺乏症候群（AIDS）的治療。
> TxGNN 模型分數最高的預測指向**猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)**——但這是獼猴的動物疾病模型，並非人類臨床適應症。
> 目前有 **20 篇文獻**支持（全數為臨床前動物實驗），**無任何人體臨床試驗**登記於此適應症下。

⚠️ **重要提醒**：此候選的「新適應症」本質上是動物疾病，不具備直接的人類臨床意義，僅可作為 AZT 抗反轉錄病毒機轉的臨床前驗證證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染／AIDS（依證據包內試驗與文獻記錄推斷；本地許可證資料缺失） |
| 預測新適應症 | 猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（臨床前動物研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料——本藥物的 `original_moa` 欄位標記為資料缺口。不過從證據包內的試驗與文獻紀錄可清楚確認：Zidovudine（3'-azido-3'-deoxythymidine, AZT）是核苷類反轉錄酶抑制劑，其磷酸化後之三磷酸鹽形式可競爭性抑制 HIV 反轉錄酶，此療效已被大量人體研究證實（例如證據包內列出的 NCT00000705「AZT 治療血友病患者 HIV 感染之第一期試驗」、NCT00001104「AZT 治療血友病患者 HIV 感染安慰劑對照試驗」等）。

TxGNN 排名第一的預測適應症「猴免疫缺陷病毒感染」在機轉上與 HIV 感染高度相似——SIV 與 HIV 同屬靈長類慢病毒（lentivirus），其反轉錄酶結構與 HIV-1 RT 有相當同源性，AZT 對兩者皆具抑制活性。但根據證據包提供的 rationale 明確指出：**「SIV 為動物（獼猴）逆轉錄病毒感染模型，非人類疾病。Zidovudine 對 SIV RT 之抑制機轉與 HIV 類似，但此為 preclinical 動物模式證據，用於支持 HIV 適應症而非獨立人類適應症。」**

換言之，這個高分預測更適合解讀為：TxGNN 模型正確捕捉到 AZT 抗反轉錄病毒的分子機轉相似性，但知識圖譜未能區分「動物疾病模型」與「人類臨床適應症」。若要讓此類預測產生臨床價值，應轉向證據包中排名第 5 的「congenital human immunodeficiency virus（先天性HIV感染）」——該項目才是具備大量已完成人體臨床試驗（如 ACTG 076 相關研究、NCT00386230 泰國圍產期短程 ZDV 研究）的真正人類適應症延伸。

---

## 臨床試驗證據

目前無相關臨床試驗登記（本適應症之 `clinical_trials` 與 `ictrp_trials` 皆為空陣列——所有已知的 AZT/SIV 研究均為動物實驗，未登記於人體臨床試驗資料庫）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | 動物實驗 | Antimicrob Agents Chemother | 新生恆河猴 SIV 感染模式：口服 AZT 可預防 SIV 感染 |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | 動物實驗 | AIDS (London) | 陰道暴露後以 AZT+3TC+Indinavir 三合一預防獼猴 SIV 感染 |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | 動物實驗 | AIDS Res Hum Retroviruses | AZT 治療對食蟹獼猴急性 SIV 感染病毒量的影響，作為抗慢病毒治療動物模式 |
| [22713337](https://pubmed.ncbi.nlm.nih.gov/22713337/) | 2012 | 動物實驗（比較藥物） | Antimicrob Agents Chemother | 新型 NRTI 對 SIV 之體外及體內反應，含 AZT 作為對照藥物 |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | 動物實驗 | J Virol | SHIV 感染獼猴骨髓造血功能缺損，即使含 AZT 之 HAART 有效降低病毒量仍存在 |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | 動物實驗 | Antimicrob Agents Chemother | 新生獼猴立即給予 AZT 可預防 SIV 感染或降低快速進展為 AIDS 之風險 |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | 動物實驗 | J Infect Dis | AZT 治療延長 SIV 週產期感染獼猴存活時間並降低中樞神經系統病毒量 |
| [8101673](https://pubmed.ncbi.nlm.nih.gov/8101673/) | 1993 | 動物實驗 | Virology | 豬尾獼猴急性 HIV-1 感染模式，作為靈長類慢病毒感染背景研究 |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | 動物實驗 | J Virol | 四重抗反轉錄病毒治療對 SIV 感染獼猴之快速病毒衰減動力學 |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | 動物實驗（抗藥性） | Antimicrob Agents Chemother | AZT 抗藥性 SIV 突變株（Q151M）仍可致新生獼猴 AIDS，顯示抗藥性演化風險 |

---

## 香港上市資訊

目前無許可證資料——本藥物於香港未上市（`total_licenses` 為 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本證據包中 `key_warnings`、`contraindications` 及藥物交互作用資料皆缺失，且 DDI 查詢無結果）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症「猴免疫缺陷病毒感染」是動物疾病模型而非人類臨床適應症，即使 TxGNN 分數高達 99.96%，也不具備直接可推進的臨床開發價值。
- 現有 20 篇支持文獻全數為臨床前動物實驗（證據等級 L4），無任何人體臨床試驗，決策階段停留於 S0。
- 安全性資料存在 Blocking 等級缺口（TFDA/香港仿單警語與禁忌症未取得），依規則無法進入 S1 安全性初評。

**若要推進需要：**
- 取得原廠仿單警語與禁忌症資料，補齊 Blocking 缺口（DG001）後方可進行 S1 安全性初評
- 補充完整作用機轉（MOA）資料（DG002），以強化機轉關聯性分析
- 建議將評估焦點轉向證據包排名第 5 之候選「先天性人類免疫缺陷病毒感染 (congenital HIV)」——該項目已有多個已完成人體 Phase 3 試驗（如圍產期垂直傳染預防相關研究），臨床意義與證據強度遠高於排名第一之動物疾病預測
- 釐清香港上市狀態與可及性，本藥物目前無許可證，需另行評估上市路徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

