---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 5
---

# Milrinone
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

# Milrinone：從原適應症（許可證未載明）到禿髮 (Alopecia)

## 一句話總結

Milrinone 是一種 PDE3 抑制劑，在香港有 3 張注射劑許可證，但許可證資料未載明原適應症。
TxGNN 模型預測它可能對**禿髮 (Alopecia)** 有效（預測分數 99.91%）。
目前該適應症**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 禿髮 (Alopecia) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Milrinone 是 PDE3 抑制劑，會提高細胞內 cAMP 並造成血管擴張。理論上，這可能與毛囊血流灌注或 cAMP 訊號有關，但這只是推測，沒有任何研究證實。

TxGNN 的高分很可能來自知識圖譜中與其他落髮相關疾病節點的相近性，而不是實際的藥理證據。

TxGNN 的前四名預測都是毛髮相關疾病，分數皆為 99.89% 至 99.91%：

| 排名 | 預測疾病 | 分數 | 機轉評估 |
|------|---------|------|---------|
| 1 | 禿髮 (Alopecia) | 99.91% | 可設想與毛囊灌注或 cAMP 訊號有關，但屬推測 |
| 2 | 頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp) | 99.90% | 罕見遺傳性毛髮疾病，PDE3 抑制與其基因缺陷無合理關聯 |
| 3 | 先天性毛髮稀少伴粟丘疹 (Congenital hypotrichosis milia) | 99.89% | 罕見先天疾病，無已知機轉關聯 |
| 4 | 瀰漫性圓形禿 (Diffuse alopecia areata) | 99.88% | 屬自體免疫疾病，cAMP 升高有一般免疫調節作用，但無證據連結 Milrinone |

以上四項皆無臨床試驗與文獻，證據等級均為 L5。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 補充：唯一有間接證據的預測（頭痛疾患）

TxGNN 排名第 5 的**頭痛疾患 (Headache disorder)**，預測分數為 99.46%，是這批預測中唯一有間接證據的。證據等級為 L4，建議為「研究問題」（Research Question）。

證據來自**可逆性腦血管收縮症候群 (RCVS)**，這是造成雷擊式頭痛的原因之一。Milrinone 的血管擴張作用，曾被用於靜脈或動脈內給藥以緩解 RCVS 的腦血管痙攣。這個證據只針對 RCVS 背後的血管收縮，不能推論到一般頭痛疾患。

| 類型 | 編號 | 年份 | 主要發現 |
|------|------|------|---------|
| 文獻 | [34784343](https://pubmed.ncbi.nlm.nih.gov/34784343/) | 2021 | 病例報告：子癇背景下的 RCVS，Milrinone 輸注後有反應（期刊：The American Journal of Case Reports） |
| 文獻 | [18647181](https://pubmed.ncbi.nlm.nih.gov/18647181/) | 2009 | 病例報告：口服鈣離子阻斷劑無效的 RCVS 患者，接受動脈內 Milrinone 治療（期刊：Headache） |
| 文獻 | [25440342](https://pubmed.ncbi.nlm.nih.gov/25440342/) | 2015 | 病例系列：RCVS 診斷方法，不確定與 Milrinone 直接相關（期刊：Journal of Stroke and Cerebrovascular Diseases） |
| 試驗 | [NCT06205758](https://clinicaltrials.gov/study/NCT06205758) | 2023 起 | N/A 階段、狀態未知、1,600 人，比較 Milrinone 與 Levosimendan 用於急性心臟衰竭合併腎功能不全。研究對象是心臟病患，與頭痛無關，僅列參考 |

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-67864 | MILRICOR SOLUTION FOR INJECTION/INFUSION 10MG/10ML | PHARM HEALTHCARE ASIA LIMITED |
| HK-68587 | MILRINONE LACTATE INJECTION USP 10MG/10ML | CHEMILL PHARMA LIMITED |
| HK-36347 | PRIMACOR INJ 1MG/ML | SANOFI HONG KONG LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

針對頭痛／RCVS 方向，需特別留意 Milrinone 可能引起低血壓，這在腦部低灌注與子癇等情境下需要謹慎。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 禿髮預測分數雖高（99.91%），但沒有任何臨床試驗或文獻，也沒有作用機轉資料，證據等級僅為 L5，不足以推進。
- 頭痛疾患（RCVS）方向有少量病例報告，但屬間接證據，且與原預測的禿髮無關。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料。
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症。
- 針對禿髮：先做文獻與前臨床檢索，確認 PDE3 抑制或 cAMP 訊號與毛囊生物學是否有關。
- 針對頭痛（RCVS）：另立研究問題，先做系統性文獻回顧，並評估低血壓風險。
- 確認給藥途徑的可行性。目前僅有注射劑，若用於禿髮是否需要外用劑型尚待評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

