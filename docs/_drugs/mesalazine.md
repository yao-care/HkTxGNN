---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 567
evidence_level: L5
indication_count: 6
monitor_inn: "MESALAZINE"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
last_modified_at: 2026-10-28
description: "Mesalazine：預測新適應症為先天性少毛症合併青少年黃斑部失養症 (congenital hypotrichosis with juvenile macular dys…（證據等級 L5）。原適應症：知識圖譜記錄的關聯：潰瘍性結腸炎、發炎性腸道疾病、潰瘍性直腸乙狀結腸炎"
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Mesalazine：從潰瘍性結腸炎到先天性少毛症合併青少年黃斑部失養症
{: .text-alpha }

## 一句話總結

Mesalazine（美沙拉嗪，5-ASA）在知識圖譜中記錄的原有用途為潰瘍性結腸炎、發炎性腸道疾病與潰瘍性直腸乙狀結腸炎。
TxGNN 模型預測分數最高的是**先天性少毛症合併青少年黃斑部失養症**，但該預測缺乏任何生物學依據；證據相對最多的是**類風濕性關節炎 (Rheumatoid Arthritis)**。
針對任何預測疾病，目前皆**無臨床試驗**，也沒有直接研究 mesalazine 用於該疾病的文獻。

> 說明：依預測排名，第 1 名為先天性少毛症合併青少年黃斑部失養症（證據為 L5，無任何研究）。本報告以第 1 名為主要預測，並在後文補充其他候選疾病的比較。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：潰瘍性結腸炎、發炎性腸道疾病、潰瘍性直腸乙狀結腸炎（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 先天性少毛症合併青少年黃斑部失養症 (congenital hypotrichosis with juvenile macular dystrophy) |
| TxGNN 預測分數 | 0.9965 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 核准數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 mesalazine 具抗發炎作用，可能涉及抑制 COX/LOX、活化 PPAR-γ 與調節 NF-κB。

先天性少毛症合併青少年黃斑部失養症是由 CDH3 基因突變引起的罕見遺傳疾病，影響毛囊與視網膜。其致病機轉為 cadherin-3 缺陷，與 mesalazine 的抗發炎作用沒有已知關聯。此高分（0.9965）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

### 其他候選疾病比較

| 預測疾病 | TxGNN 分數 | 證據等級 | 說明 |
|---------|-----------|---------|------|
| 骨關節炎 | 0.9963 | L5 | 僅有一篇轉錄體計算分析，非臨床證據；可能透過 NF-κB、前列腺素與白三烯路徑調節發炎，關聯性薄弱 |
| 類風濕性關節炎 | 0.9957 | L5 | 見下方說明 |
| 脂漏性角化症 | 0.9950 | L5 | 無機轉依據，無研究 |
| 外陰倒置性毛囊角化症 | 0.9933 | L5 | 無機轉依據，無研究 |
| 假性軟骨發育不全 | 0.9919 | L5 | 與 COMP 突變相關，mesalazine 無已知作用 |

**類風濕性關節炎**：現有文獻多為柳氮磺吡啶 (sulfasalazine) 的回顧、藥動學、不良反應通報與病例報告。柳氮磺吡啶會釋出 5-ASA 與 sulfapyridine，但抗風濕效果一般歸因於 sulfapyridine 而非 5-ASA，因此不能支持 mesalazine 單獨有效。所列文獻中沒有直接研究 mesalazine 治療類風濕性關節炎的研究，故證據等級維持 L5。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對第 1 名預測疾病（先天性少毛症合併青少年黃斑部失養症），目前無相關文獻。

以下為證據相對最多的類風濕性關節炎的主要文獻（均非直接研究 mesalazine 對該病的療效）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | 回顧柳氮磺吡啶用於類風濕性關節炎的藥理與療效，其分解產物含 mesalazine，但活性成分尚不確定 |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review | Dtsch Med Wochenschr | Mesalazine 藥物回顧（無摘要） |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | 慢作用抗風濕藥（含柳氮磺吡啶）的藥動學 |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | 藥物安全監測分析 | Gut | 重新評估柳氮磺吡啶與 mesalazine 的嚴重不良反應通報 |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2026 | Case report | Intern Med | 類風濕性關節炎患者發生 5-ASA 誘發的結腸炎 |
| [31830393](https://pubmed.ncbi.nlm.nih.gov/31830393/) | 2019 | Case report | G Ital Nefrol | 類風濕性關節炎患者使用 mesalazine 後出現 DRESS 症候群合併急性腎衰竭 |
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | 計算／轉錄體分析 | J Transl Med | 骨關節炎治療標靶的計算預測，非臨床證據 |

---

## 香港上市資訊

已上市，目前列出 20 張單一成分許可證（清單可能不完整，實際至少 20 張）。許可證資料未載明核准適應症與劑型，以下僅列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63749 | SYN-MESALAZINE ENTERIC-COATED TABLETS 250MG | 腸溶錠 | 許可證資料未載明 |
| HK-37044 | PENTASA SUPP 1G | 栓劑 | 許可證資料未載明 |
| HK-65052 | SALOFALK GASTRO-RESISTANT PROLONGED-RELEASE GRANULES 1.5G | 抗胃酸緩釋顆粒 | 許可證資料未載明 |
| HK-51119 | ASACOL ENEMA 4G/100ML | 灌腸劑 | 許可證資料未載明 |
| HK-59673 | SALOFALK 250 SUPP 250MG | 栓劑 | 許可證資料未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、肝臟疾病、膽囊疾病、嗜中性白血球減少、顆粒球缺乏症、貧血（含巨球性貧血）、幽門狹窄、脂質性腎病變、間質性腎炎、輸尿管積膿。
- **藥物交互作用**：資料庫共記錄 100 筆。
  - 嚴重 (Major)：Cidofovir、人類肉毒桿菌神經毒素 A/B 免疫球蛋白
  - 中度 (Moderate)：Ketorolac、Ibuprofen、Celecoxib（NSAID 類）、Acyclovir、Amphotericin B、Amikacin、Azathioprine、Cisplatin 等，多與腎毒性疊加有關
- **文獻中的安全警訊**：與類風濕性關節炎相關的文獻顯示 5-ASA 可能引發腎毒性、DRESS 症候群與藥物性結腸炎。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測疾病均無臨床試驗，也沒有直接研究 mesalazine 對該疾病的文獻，證據等級均為 L5。
- 最高分的預測（先天性少毛症合併青少年黃斑部失養症 0.9965、假性軟骨發育不全 0.9919 等）為罕見遺傳疾病，無機轉關聯，分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。類風濕性關節炎的間接證據來自柳氮磺吡啶，無法推論 mesalazine 單獨有效。

**若要推進需要：**
- 取得 mesalazine 的作用機轉資料（MOA）
- 取得香港仿單的警語、禁忌與核准適應症文字
- 針對類風濕性關節炎或骨關節炎，進行 mesalazine 單藥與 sulfapyridine 成分的比較性文獻回顧與前臨床研究
- 對高分但無機轉依據的罕見疾病預測，不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

