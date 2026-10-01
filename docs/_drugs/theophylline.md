---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 856
evidence_level: L5
indication_count: 5
---

# Theophylline
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

# Theophylline：從支氣管擴張劑（氣喘／慢性呼吸道疾病）到血栓性疾病

## 一句話總結

Theophylline（茶鹼）是一種支氣管擴張劑，文獻記載用於氣喘、支氣管炎與肺氣腫。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic Disease)** 有效，分數很高（99.62%）。
但目前**沒有任何臨床試驗**，現有文獻也與此用途無直接關聯，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；文獻描述為支氣管擴張劑（氣喘、支氣管炎、肺氣腫） |
| 預測新適應症 | 血栓性疾病 (Thrombotic Disease) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Theophylline 是甲基黃嘌呤類藥物，在呼吸道疾病中的用途已有長期文獻記載。以下機轉只是推測，現有文獻並未證實：它可能透過抑制磷酸二酯酶 (PDE) 與拮抗腺苷受體，提高血小板內的 cAMP，進而抑制血小板活化。

血小板活化是動脈血栓形成的重要環節，所以這個方向在機轉上說得通。不過證據包內的 10 篇文獻都不是在研究 theophylline 的抗血栓作用。內容包括 ticlopidine 藥動學、血小板與生物標記檢測方法、theophylline 偵測感測器、腦水腫等，因此模型預測目前沒有獨立佐證。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

以下文獻皆為間接相關，沒有任何一篇直接評估 theophylline 用於血栓性疾病。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | 藥動學回顧（其他藥物：ticlopidine） | Clin Pharmacokinet | 說明抗血小板藥 ticlopidine 的藥動學，與 theophylline 無直接關係 |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | 前列腺素與血小板的關係：前列環素提高血小板 cAMP 而抑制聚集，提供背景機轉 |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 體外研究 | Gen Pharmacol | Milrinone 與腺苷透過提高 cAMP 抑制人類血小板反應（非 theophylline） |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | 體外研究 | J Nutr | 陳年大蒜萃取物透過 cAMP/cGMP 訊號抑制血小板聚集（非 theophylline） |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | 檢測方法 | Br J Haematol | 血小板第四因子放射免疫分析；theophylline 僅作為採血抗凝劑成分 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 分析方法 | Anal Chim Acta | Theophylline 偵測感測器；指出藥物濃度過高有毒性，需嚴格監測 |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | 檢測方法 | Platelets | 血漿可溶性 CLEC-2 可作為血小板活化標記，與血栓風險評估相關 |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | 觀察性研究 | Cor Vasa | 心肌梗塞與血栓性靜脈炎患者的 theophylline 抗性 T 細胞比例增加（以 theophylline 作為細胞分型工具） |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | 臨床論述（德文） | Z Gesamte Inn Med | 血栓栓塞疾病導致的慢性肺心症；無摘要可供判讀 |
| [29956444](https://pubmed.ncbi.nlm.nih.gov/29956444/) | 2018 | 基礎研究 | J Thromb Haemost | 內皮細胞 Weibel-Palade 小體的分泌調控，屬止血與發炎的基礎生物學 |

## 香港上市資訊

香港共登記 8 張許可證，以下列出其中 5 張主要許可證。證據包未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-45955 | SLO-THEO CAP 100MG (EXTENDED-RELEASE) | PRIMAL CHEMICAL CO LTD |
| HK-45954 | SLO-THEO CAP 50MG (EXTENDED-RELEASE) | PRIMAL CHEMICAL CO LTD |
| HK-19359 | NUELIN-SR 125 TAB 125MG S R WHITE | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-45831 | NUELIN SR 200 TAB 200MG (INDIA) | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-45832 | NUELIN SR 300 TAB 300MG (INDIA) | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

補充：證據包內的文獻（PMID 29254574）指出，theophylline 在血中濃度過高時有毒性，使用時需嚴格監測。

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 分數雖高，但沒有任何臨床試驗，現有文獻也沒有直接支持 theophylline 抗血栓作用的內容，證據等級僅 L5。此外，香港仿單的警語與禁忌症資料缺漏（資料缺口 DG001，屬阻斷性），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症
- 補充 theophylline 的作用機轉資料（例如查詢 DrugBank）
- 針對 theophylline 與血小板功能／血栓的直接證據（體外血小板聚集、動物模型、人體研究）做專項文獻檢索
- 治療窗狹窄，需規劃血中濃度監測與藥物交互作用管理

**其他預測適應症（供優先排序參考）：**
- **鼻腔疾病（L2，Research Question）**：有 1 個已完成的 Phase 2 試驗 [NCT03990766](https://clinicaltrials.gov/study/NCT03990766)，為鼻用 theophylline 沖洗治療病毒感染後嗅覺障礙，樣本僅 27 人，且隨機與盲性設計、療效結果皆需再確認。
- **阻塞性肺病（L3，Proceed with Guardrails）**：有多篇氣喘與 COPD 的臨床研究和回顧文獻，現有證據包中的登記試驗多為觀察性研究或其他吸入藥物研究，無法確認為 theophylline 療效試驗，因此等級上限為 L3。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

