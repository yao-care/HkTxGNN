---
layout: default
title: Flunitrazepam
parent: 中證據等級 (L3-L4)
nav_order: 386
evidence_level: L3
indication_count: 5
last_modified_at: 2026-10-14
description: "Flunitrazepam：預測新適應症為失眠 (Insomnia)（證據等級 L3）。原適應症：資料未提供"
monitor_inn: "FLUNITRAZEPAM"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "anxiety", "anxiety disorder"]
---

# Flunitrazepam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Flunitrazepam：從失眠到失眠（模型預測與既有用途重疊）

## 一句話總結

Flunitrazepam 是一種苯二氮平類（benzodiazepine）藥物，臨床上主要作為助眠藥與麻醉前鎮靜劑。
TxGNN 模型預測的首位適應症為**失眠 (Insomnia)**，但這其實是該藥已確立的用途，並非真正的新適應症。
目前**無臨床試驗登記**，有 **10 篇文獻**支持失眠這個方向。真正屬於「新用途」的預測（偏頭痛、焦慮）證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明核准適應症文字） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

其他預測適應症：偏頭痛（99.71%，L5，Hold）、伴腦幹先兆的偏頭痛（99.63%，L5，Hold）、焦慮（99.63%，L4）、焦慮症（99.58%，L4）。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據藥理學資料，Flunitrazepam 作用於 GABA-A 受體 α1、α2、α3、α5 亞單位，屬於正向異構調節劑，可增強抑制性神經傳導，促進鎮靜與入睡。

這與助眠用途直接吻合。需特別說明：失眠本來就是此藥在許多國家的既有用途，因此這個預測**不是真正的藥物再利用訊號**，而是模型重現了已知知識。

至於焦慮，GABA-A 調節確實是苯二氮平類抗焦慮作用的基礎，機轉上合理；但已有許多苯二氮平類藥物獲准用於焦慮，Flunitrazepam 的濫用與依賴風險較高，相較之下缺乏優勢。偏頭痛的預測僅來自模型，沒有任何文獻佐證，且苯二氮平類並不建議用於偏頭痛。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為失眠方向的文獻（依類型排序，最多 10 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | 臨床比較研究 | Eur Respir J | 比較 zolpidem、triazolam、flunitrazepam 對重度 COPD 患者血氣與呼吸控制的影響 |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | 臨床研究 | JAMA | 停用 flunitrazepam、nitrazepam、triazolam 後出現反彈性失眠 |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | 臨床研究 | Sleep Med Rev | 助眠藥影響身體平衡與站立穩定度，增加跌倒與髖部骨折風險 |
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | 臨床研究 | Nouv Presse Med | 探討 flunitrazepam 對器質性與功能性睡眠障礙的作用 |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Triazolam 的藥理與療效回顧，並與 flunitrazepam 等長效藥比較 |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatr Scand Suppl | 老年人對苯二氮平類的反應增強約 2–3 倍，且無法單純以血中濃度解釋 |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | 助眠藥的臨床使用適應症與多樣化選擇的必要性 |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | 動物前臨床 | Psychopharmacology | 在睡眠障礙大鼠模型中比較三種助眠藥對睡眠-清醒週期的影響 |

另有 2 篇與主題關聯較低的文獻（植物萃取物動物研究、良性復發性肝內膽汁淤積個案報告）已略去。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56628 | FLUNITA TAB 1MG | 錠劑 | 未載明 |
| HK-34683 | FLUNITA TAB 2MG | 錠劑 | 未載明 |
| HK-12370 | ROHYPNOL TAB 1MG | 錠劑 | 未載明 |

---

## 安全性考量

- **藥物交互作用／藥理標靶**：主要作用於 GABA-A 受體 α1、α2、α3、α5 亞單位。已整理的資料中未列出具體的藥物對藥物交互作用。
- **文獻提示的風險**：
  - 停藥後反彈性失眠
  - 平衡與姿勢穩定度受損，增加跌倒風險
  - 呼吸抑制（尤其是 COPD 患者）
  - 耐受性與依賴性
  - 高濫用潛力，曾有被用於藥物助長犯罪（「約會強暴藥」）的報告
  - 記憶損害（順行性失憶）與駕駛能力受損
  - 少數個案出現矛盾反應（激動、攻擊行為）

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 失眠是 Flunitrazepam 的既有用途，有多篇臨床研究與回顧支持（證據等級 L3），且香港已有 3 張有效許可證。但這不構成新的再利用機會。
- 真正的新適應症（偏頭痛、焦慮）僅有模型預測或間接文獻，且存在依賴與濫用風險，不建議推進（偏頭痛為 Hold；焦慮列為研究問題）。

**若要推進需要：**
- 取得香港衛生署核准仿單，確認核准適應症、警語與禁忌症
- 補充詳細作用機轉資料
- 若關注焦慮用途，需與已獲准的其他苯二氮平類進行比較，並提供隨機對照試驗證據
- 建立使用管控措施（處方限制、療程長度、老年與呼吸疾病患者的監測、濫用防範）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

