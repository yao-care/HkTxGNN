---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Haloperidol：預測新適應症為岩藻糖化缺陷型先天性醣基化異常 (congenital disorder of glycosylation with defective…（證據等級 L5）。原適應症：精神病性障礙、思覺失調症、思覺失調樣障礙、情感性思覺失調症、妥瑞氏症"
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Haloperidol
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

# Haloperidol：從精神病性障礙到醣基化先天異常（岩藻糖化缺陷型）

## 一句話總結

Haloperidol 是一種典型抗精神病藥物，原本用於思覺失調症、精神病性障礙及妥瑞氏症等。
TxGNN 模型預測它可能對**岩藻糖化缺陷型先天性醣基化異常 (congenital disorder of glycosylation with defective fucosylation)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 精神病性障礙、思覺失調症、思覺失調樣障礙、情感性思覺失調症、妥瑞氏症（依知識圖譜資料） |
| 預測新適應症 | 岩藻糖化缺陷型先天性醣基化異常 (congenital disorder of glycosylation with defective fucosylation) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Haloperidol 是多巴胺 D2 受體拮抗劑，這也是它在精神病治療中的主要藥理作用。

然而，D2 受體阻斷與岩藻糖化途徑（例如 GDP-岩藻糖轉運、SLC35C1）之間，並沒有已知的關聯。原適應症屬於精神神經疾病，而預測的新適應症是代謝／醣基化的遺傳性疾病，兩者在病理上幾乎沒有交集。

因此，這個高分預測較可能是知識圖譜運算下的假象（artifact），而非真正有生物學依據的發現。

### 其他排名較前的預測（供參考）

| 排名 | 預測疾病 | 分數 | 證據等級 | 評估 |
|------|---------|------|---------|------|
| 2 | 視網膜失養症（伴或不伴眼外異常） | 99.91% | L4 | 僅有 2 篇大鼠前臨床研究，屬對正常視網膜生理的影響，並非治療獲益證據；多巴胺拮抗甚至可能不利視網膜功能 |
| 3 | 無腦迴畸形／水腦無腦症 (hydranencephaly) | 99.90% | L5 | 結構性先天畸形，D2 拮抗劑無合理作用 |
| 4 | X 連鎖近視 | 99.89% | L5 | 多巴胺促效通常有保護作用，拮抗劑反而可能促進近視惡化 |
| 5 | 夏柯-馬利-杜斯氏症 1G 型 | 99.89% | L5 | 與髓鞘維持無關，且 Haloperidol 的錐體外症候群副作用對神經病變族群不利 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（岩藻糖化缺陷型先天性醣基化異常），目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64839 | HALOPERIDOL-NEURAXPHARM TABLETS 1MG | — | 未提供 |
| HK-54962 | HALOPERIDOL INJ 5MG/ML | — | 未提供 |
| HK-65060 | HALOPERIDOL-NEURAXPHARM DECANOATE SOLUTION FOR INJECTION 100MG/ML | — | 未提供 |
| HK-65430 | HALOPERIDOL-NEURAXPHARM TABLETS 5MG | — | 未提供 |
| HK-62669 | HALOPERIDOL KERN PHARMA ORAL DROPS 2MG/ML | — | 未提供 |

共 18 張有效單一成分許可證（無已註銷者），以上僅列出 5 張。

---

## 安全性考量

- **禁忌／高風險疾病（來自知識圖譜，非仿單內容）**：
  - 心臟：長 QT 症候群（含家族性）、尖端扭轉型心律不整
  - 神經：癲癇、基底核疾病、局部手部肌張力不全、眼瞼痙攣、抗精神病藥物惡性症候群
  - 血液：嗜中性白血球低下、顆粒球缺乏症、白血球低下及多種先天性嗜中性白血球低下症
  - 其他：肝病、膽囊疾病、甲狀腺功能低下／黏液水腫、缺鉀、低血壓、女性乳癌
- **藥物交互作用**：共查得 100 筆，以下為部分重點：
  - **嚴重（Major）**：Bupropion、Morphine、Clarithromycin、Dolasetron
  - **中度（Moderate）**：Famotidine、Epinephrine、Hydrocortisone、Amphotericin B、Hyoscyamine、Loperamide、Aprepitant、Atropine 等

完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅有模型分數支持（L5），沒有臨床試驗與文獻；機轉上也找不到 D2 阻斷與岩藻糖化途徑的關聯，分數極可能是圖譜假象。
- Haloperidol 有 QT 延長、錐體外症候群、血液學異常等明確風險，在缺乏療效依據下不宜推進。

**若要推進需要：**
- 提出可驗證的生物學假說（例如 D2 訊息與岩藻糖化／GDP-岩藻糖轉運的關聯），並做體外或前臨床驗證
- 補齊作用機轉資料與香港仿單的警語、禁忌
- 另可評估第 2 名（視網膜失養症）的後續研究，但現有大鼠資料並未顯示治療獲益，且存在潛在不利風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

